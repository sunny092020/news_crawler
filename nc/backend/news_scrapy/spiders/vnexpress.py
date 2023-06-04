import scrapy
from news_scrapy.settings import (
    VNEXPRESS_SELECTORS,
    VNEXPRESS_CATEGORY_MAPPING,
    FALLBACK_CATEGORY,
    ARTICLE_FROM_DATE,
)
from news_scrapy.items import ArticleItem
from datetime import datetime
from bs4 import BeautifulSoup
import html


class VnexpressSpider(scrapy.Spider):
    name = "vnexpress"
    allowed_domains = ["vnexpress.net"]
    start_urls = ["https://vnexpress.net/rss"]

    def parse(self, response):
        # Extract all sub RSS feed links
        for href in response.xpath('//a[contains(@href, "rss")]/@href').getall():
            url = response.urljoin(href)
            yield scrapy.Request(url, callback=self.parse_rss)

    def parse_rss(self, response):
        # Extract details from each article in a sub RSS feed
        for post in response.xpath("//item"):
            article_url = post.xpath("link/text()").get()
            title = html.unescape(post.xpath("title/text()").get())
            description = html.unescape(extract_text(post.xpath("description/text()").get()))
            pub_date = post.xpath("pubDate/text()").get()
            pub_date = parse_datetime(pub_date)
            specific_date = parse_datetime(ARTICLE_FROM_DATE)

            if article_url and pub_date >= specific_date:
                yield scrapy.Request(
                    article_url,
                    callback=self.parse_article,
                    cb_kwargs={
                        "title": title,
                        "description": description,
                        "pub_date": pub_date,
                    },
                )

    def parse_article(self, response, title, description, pub_date):
        item = ArticleItem()
        item["title"] = title
        item["url"] = response.url
        item["content"] = (
            response.css(VNEXPRESS_SELECTORS["content"]).get()
            or response.css(VNEXPRESS_SELECTORS["video_content"]).get()
        )
        item["site"] = self.name
        item["published_date"] = pub_date
        item["author"] = response.css(VNEXPRESS_SELECTORS["author"]).get()
        item["summary"] = description

        raw_category = response.css(VNEXPRESS_SELECTORS["category"]).get()
        internal_category_name = VNEXPRESS_CATEGORY_MAPPING.get(
            raw_category, FALLBACK_CATEGORY
        )

        item["category"] = internal_category_name

        yield item


def parse_datetime(date_string):
    return datetime.strptime(date_string, "%a, %d %b %Y %H:%M:%S %z")


def extract_text(description):
    soup = BeautifulSoup(description, "lxml")
    return soup.get_text()
