import scrapy


class VnexpressSpider(scrapy.Spider):
    name = "vnexpress"
    allowed_domains = ["vnexpress.net"]
    start_urls = ["http://vnexpress.net/"]

    def parse(self, response):
        pass
