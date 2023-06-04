import scrapy
from news_scrapy.settings import (
    VNEXPRESS_SELECTORS,
    VNEXPRESS_CATEGORY_MAPPING,
    FALLBACK_CATEGORY,
)
import logging
from dateutil.parser import parse
import datetime
import pytz
from news_scrapy.items import ArticleItem


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
            if article_url:
                yield scrapy.Request(article_url, callback=self.parse_article)

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
