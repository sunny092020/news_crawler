from news_scrapy.spiders.vnexpress_selenium import VnexpressSpiderSelenium

spider = VnexpressSpiderSelenium()
spider.start_requests()  # start the scraping
items = spider.close()  # close the browser when you're done
