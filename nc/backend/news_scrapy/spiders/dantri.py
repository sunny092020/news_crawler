import scrapy
from news_scrapy.settings import DANTRI_SELECTORS
from news_scrapy.items import ArticleItem
import logging
from dateutil.parser import parse


class DantriSpider(scrapy.Spider):
    name = "dantri"
    allowed_domains = ["dantri.com.vn"]
    start_urls = [
        "https://dantri.com.vn/",
    ]

    def parse(self, response):
        # Follow all links on the main_nav or nav_folder
        main_nav_links = response.css(DANTRI_SELECTORS["main_nav"]).getall()
        sub_nav_links = response.css(DANTRI_SELECTORS["sub_nav"]).getall()
        nav_folder_links = response.css(DANTRI_SELECTORS["nav_folder"]).getall()

        links = main_nav_links + sub_nav_links + nav_folder_links

        for link in links:
            # Skip javascript links
            if "javascript" in link.lower():
                continue

            # Skip links mail to
            if "mailto" in link.lower():
                continue

            # Skip links to tel
            if "tel:" in link.lower():
                continue

            yield response.follow(link, self.parse)

        for article in response.css(DANTRI_SELECTORS["article"]).getall():
            logging.debug("Article: %s", article)
            yield response.follow(article, self.parse_article)

    def parse_article(self, response):
        item = ArticleItem()
        item["title"] = response.css(DANTRI_SELECTORS["title"]).get()
        item["url"] = response.url
        item["content"] = response.css(DANTRI_SELECTORS["content"]).get()
        item["site"] = "vnexpress.net"

        item["published_date"] = response.css(DANTRI_SELECTORS["publication_date"]).get()

        item["author"] = response.css(DANTRI_SELECTORS["author"]).get()
        item["summary"] = response.css(DANTRI_SELECTORS["summary"]).get()

        yield item
