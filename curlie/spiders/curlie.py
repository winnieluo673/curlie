import scrapy
from urllib import parse
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from curlie.items import CurlieItem

class CurlieSpider(CrawlSpider):
    name = "curlie"
    allowed_domains = ["curlie.org"]
    start_urls = ["https://curlie.org/News/"]
    rules =(
         Rule(LinkExtractor(allow=(r'https://curlie.org/News/[\s\S]*'),restrict_xpaths = ('//section[@class="children"]//div[@class="cat-item"]')), callback="parse_item" ,follow=True),#只爬News路径下的
        #Rule(LinkExtractor(restrict_xpaths=('//section[@class="children"]//div[@class="cat-item"]')),callback="parse_item", follow=True), #News子分类下的都爬
    )

    def parse_item(self,response):
        item = CurlieItem()
        #当前所属目录分类
        item['category'] = response.url.lstrip('https://curlie.org')

        #当前目录子目录
        item['subcategory'] = []
        for sub in response.xpath('//section[@class="children"]//div[@class="cat-item"]'):
            subcategory = {}
            subcategory['name'] = sub.xpath('.//a/div/text()').extract()[1].strip()
            subcategory['url'] = parse.urljoin(response.url, sub.xpath('.//a/@href').extract_first())
            item['subcategory'].append(subcategory)

        #当前目录下的网站
        item['sites'] = []
        for site in response.xpath('//section[@class="results sites"]//div[@class="site-item "]'):
            sites = {}
            sites['title'] = site.xpath('./div[@class="title-and-desc"]/a/div/text()').extract_first()
            sites['site_url'] = parse.urljoin(response.url, site.xpath('./div[@class="title-and-desc"]/a/@href').extract_first())
            sites['description'] = site.xpath('.//div[@class="site-descr "]/text()').extract_first().strip()
            item['sites'].append(sites)
        yield item



