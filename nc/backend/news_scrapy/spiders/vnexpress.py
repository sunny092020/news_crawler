import logging
import time
from datetime import datetime
from dateutil.parser import parse
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from news_scrapy.items import ArticleItem
import pytz
from news_scrapy.settings import VNEXPRESS_SELECTORS
import traceback

class VnexpressSpiderSelenium:

    def __init__(self):
        self.driver = None
        self.wait = None
        self.start_urls = "http://vnexpress.net/"
        self.items = []

    def start_requests(self):
        # Setup Chrome options
        chrome_options = Options()
        chrome_options.add_argument("--headless")  # Ensure GUI is off
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")

        # Set path to chromedriver as per your configuration
        webdriver_service = Service('chromedriver')

        self.driver = webdriver.Chrome(service=webdriver_service, options=chrome_options)
        self.wait = WebDriverWait(self.driver, 10)

        self.driver.get(self.start_urls)
        self.parse()

    def parse(self):
        articles = self.wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, VNEXPRESS_SELECTORS['article'])))
        
        article_urls = [article.get_attribute('href') for article in articles]

        print("print Number of article_urls44: ", len(article_urls))

        try:
            for article_url in article_urls:
                self.driver.get(article_url)
                self.parse_article()
        except Exception as e:
            logging.error("logging Error: %s", e)
            print("print Error: ", e)
            traceback.print_exc()

    def parse_article(self):
        item = ArticleItem()

        item["title"] = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, VNEXPRESS_SELECTORS['title']))).text
        item["url"] = self.driver.current_url
        item["content"] = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, VNEXPRESS_SELECTORS['content']))).text
        item["site"] = "vnexpress.net"

        raw_date = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, VNEXPRESS_SELECTORS['publication_date']))).text
        logging.debug("Raw date: %s", raw_date)

        parsed_date = self.parse_date(raw_date)
        item["published_date"] = parsed_date

        item["author"] = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, VNEXPRESS_SELECTORS['author']))).text
        self.items.append(item)

    def parse_date(self, date_str):
        date_str = date_str.split(", ")[1:]
        date_str = ", ".join(date_str)
        logging.debug("Date string: %s", date_str)
        date_str = date_str.replace(" (GMT", "").replace(")", "")
        dt = parse(date_str)
        return dt.astimezone(pytz.UTC)

    def close(self):
        self.driver.quit()
        return self.items
