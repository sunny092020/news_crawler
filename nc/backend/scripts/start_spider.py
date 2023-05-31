from news_scrapy.spiders.vnexpress import VnexpressSpider

spider = VnexpressSpider()
spider.start_requests()  # start the scraping
items = spider.close()  # close the browser when you're done
