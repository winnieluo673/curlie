import scrapy
from urllib import parse
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from curlie.items import CurlieItem

class CurlieSpider(CrawlSpider):
    name = "curlie1"
    allowed_domains = ["curlie.org"]
    start_urls = ["https://curlie.org/News/"]

    def parse(self,response):
        item = CurlieItem()
        #当前所属目录分类
        item['category'] = response.url.lstrip('https://curlie.org')

        #当前目录下的网站
        item['sites'] = []
        for site in response.xpath('//section[@class="results sites"]//div[@class="site-item "]'):
            sites = {}
            sites['title'] = site.xpath('./div[@class="title-and-desc"]/a/div/text()').extract_first()
            sites['site_url'] = parse.urljoin(response.url, site.xpath('./div[@class="title-and-desc"]/a/@href').extract_first())
            sites['description'] = site.xpath('.//div[@class="site-descr "]/text()').extract_first().strip()
            item['sites'].append(sites)
        yield item



