import scrapy
from news_scrapy.settings import DANTRI_SELECTORS
from news_scrapy.items import ArticleItem
import logging
from news_scrapy.settings import DANTRI_CATEGORY_MAPPING, FALLBACK_CATEGORY
from dateutil.parser import parse
import datetime
import pytz


class DantriSpider(scrapy.Spider):
    name = "dantri"
    allowed_domains = ["dantri.com.vn"]
    start_urls = [
        "https://dantri.com.vn/",
    ]
    custom_settings = {
        "DEPTH_LIMIT": 1,
    }

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
        item["site"] = self.name

        item["published_date"] = parse_datetime(
            response.css(DANTRI_SELECTORS["publication_date"]).get()
        )

        item["author"] = response.css(DANTRI_SELECTORS["author"]).get()
        item["summary"] = response.css(DANTRI_SELECTORS["summary"]).get()

        raw_category = response.css(DANTRI_SELECTORS["category"]).get()
        logging.debug("Raw category: %s", raw_category)

        internal_category_name = DANTRI_CATEGORY_MAPPING.get(raw_category, FALLBACK_CATEGORY)
        logging.debug("Internal category: %s", internal_category_name)

        item["category"] = internal_category_name

        yield item


def parse_datetime(date_str):
    if date_str == "" or date_str is None:
        # return now with timezone
        return datetime.datetime.now(pytz.utc)
    return parse(date_str)
