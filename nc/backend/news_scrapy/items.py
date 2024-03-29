# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ArticleItem(scrapy.Item):
    title = scrapy.Field()
    url = scrapy.Field()
    content = scrapy.Field()
    site = scrapy.Field()
    published_date = scrapy.Field()
    author = scrapy.Field()
    summary = scrapy.Field()
    category = scrapy.Field()
