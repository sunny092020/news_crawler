import scrapy
from news_scrapy.settings import VNEXPRESS_SELECTORS
from news_scrapy.items import ArticleItem

class VnexpressSpider(scrapy.Spider):
    name = "vnexpress"
    allowed_domains = ["vnexpress.net"]
    start_urls = ["http://vnexpress.net/"]

    def parse(self, response):
        for article in response.css(VNEXPRESS_SELECTORS['article']).getall():
            yield response.follow(article, self.parse_article)

    def parse_article(self, response):
        item = ArticleItem()
        item.title = response.css(VNEXPRESS_SELECTORS['title']).get()
        item.url = response.url
        item.content = response.css(VNEXPRESS_SELECTORS['content']).get()
        item.source = "vnexpress.net"
        item.published_date = response.css(VNEXPRESS_SELECTORS['publication_date']).get()
        yield item
