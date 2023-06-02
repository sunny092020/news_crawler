import scrapy
from news_scrapy.settings import VNEXPRESS_SELECTORS
from news_scrapy.items import ArticleItem
import logging
from datetime import datetime
import pytz
from dateutil.parser import parse
from news_scrapy.settings import VNEXPRESS_CATEGORY_MAPPING, FALLBACK_CATEGORY


class VnexpressSpider(scrapy.Spider):
    name = "vnexpress"
    allowed_domains = ["vnexpress.net"]
    start_urls = [
        "http://vnexpress.net/",
    ]
    custom_settings = {
        "DEPTH_LIMIT": 2,
    }

    def parse(self, response):
        # Follow all links on the main_nav or nav_folder
        main_nav_links = response.css(VNEXPRESS_SELECTORS["main_nav"]).getall()
        nav_folder_links = response.css(VNEXPRESS_SELECTORS["nav_folder"]).getall()

        links = main_nav_links + nav_folder_links

        for link in links:
            # Skip javascript links
            if "javascript" in link.lower():
                continue

            # Skip links mail to
            if "mailto" in link.lower():
                continue

            yield response.follow(link, self.parse)

        for article in response.css(VNEXPRESS_SELECTORS["article"]).getall():
            logging.debug("Article: %s", article)
            yield response.follow(article, self.parse_article)

    def parse_article(self, response):
        item = ArticleItem()
        item["title"] = response.css(VNEXPRESS_SELECTORS["title"]).get()
        item["url"] = response.url
        item["content"] = (
            response.css(VNEXPRESS_SELECTORS["content"]).get()
            or response.css(VNEXPRESS_SELECTORS["video_content"]).get()
        )
        item["site"] = self.name

        raw_date = response.css(VNEXPRESS_SELECTORS["publication_date"]).get()
        logging.debug("Raw date: %s", raw_date)

        parsed_date = self.parse_date(raw_date)
        item["published_date"] = parsed_date

        item["author"] = response.css(VNEXPRESS_SELECTORS["author"]).get()
        item["summary"] = response.css(VNEXPRESS_SELECTORS["summary"]).get()

        raw_category = response.css(VNEXPRESS_SELECTORS["category"]).get()
        internal_category_name = VNEXPRESS_CATEGORY_MAPPING.get(
            raw_category, FALLBACK_CATEGORY
        )

        item["category"] = internal_category_name

        yield item

    def parse_date(self, date_str):
        try:
            # Remove the day of the week (e.g., 'Thứ tư, ')
            date_str = date_str.split(", ")[1:]
            # Rejoin the remaining parts
            date_str = ", ".join(date_str)

            logging.debug("Date string: %s", date_str)

            # Replace the space between GMT and +7 with a plus sign
            date_str = date_str.replace(" (GMT", "").replace(")", "")

            # Parse the date and time
            dt = parse(date_str)
            # Return the date in UTC
            return dt.astimezone(pytz.UTC)
        except Exception as e:
            logging.error("Error parsing date: %s", e)
            today = datetime.now()
            return today
