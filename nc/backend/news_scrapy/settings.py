# Scrapy settings for news_scrapy project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html
import os
import sys
import django

# Add the Django project to the Python path
sys.path.append(os.path.dirname(os.path.abspath(".")))

# Set the Django settings module
os.environ["DJANGO_SETTINGS_MODULE"] = "nc.settings"

# Setup Django
django.setup()


BOT_NAME = "news_scrapy"

SPIDER_MODULES = ["news_scrapy.spiders"]
NEWSPIDER_MODULE = "news_scrapy.spiders"


# Crawl responsibly by identifying yourself (and your website) on the user-agent
# USER_AGENT = "news_scrapy (+http://www.yourdomain.com)"

# Obey robots.txt rules
ROBOTSTXT_OBEY = True

# Configure maximum concurrent requests performed by Scrapy (default: 16)
# CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
DOWNLOAD_DELAY = 0
# The download delay setting will honor only one of:
# CONCURRENT_REQUESTS_PER_DOMAIN = 16
# CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
# COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
# TELNETCONSOLE_ENABLED = False

# Override the default request headers:
# DEFAULT_REQUEST_HEADERS = {
#    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
#    "Accept-Language": "en",
# }

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
# SPIDER_MIDDLEWARES = {
#    "news_scrapy.middlewares.NewsScrapySpiderMiddleware": 543,
# }

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
# DOWNLOADER_MIDDLEWARES = {
#    "news_scrapy.middlewares.NewsScrapyDownloaderMiddleware": 543,
# }

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
# EXTENSIONS = {
#    "scrapy.extensions.telnet.TelnetConsole": None,
# }

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
    "news_scrapy.pipelines.NewsScrapyPipeline": 300,
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
AUTOTHROTTLE_ENABLED = True
# The initial download delay
AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
# AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# HTTPCACHE_ENABLED = True
# HTTPCACHE_EXPIRATION_SECS = 0
# HTTPCACHE_DIR = "httpcache"
# HTTPCACHE_IGNORE_HTTP_CODES = []
# HTTPCACHE_STORAGE = "scrapy.extensions.httpcache.FilesystemCacheStorage"

# Set settings whose default value is deprecated to a future-proof value
REQUEST_FINGERPRINTER_IMPLEMENTATION = "2.7"
TWISTED_REACTOR = "twisted.internet.asyncioreactor.AsyncioSelectorReactor"
FEED_EXPORT_ENCODING = "utf-8"

VNEXPRESS_SELECTORS = {
    "main_nav": "nav.main-nav ul.parent li a::attr(href)",
    "sub_nav": "nav.main-nav ul.parent li ul.sub li a::attr(href)",
    "article": ".title_news a::attr(href)",
    "nav_folder": "ul.breadcrumbs li a::attr(href), p.cat_time a::attr(href)",
    "category": "ul.breadcrumb li a::attr(data-medium), p.cat_time a::attr(title)",
    "title": "h1.title-detail::text, h1.title::text",
    "content": "article.fck_detail",
    "video_content": "div[id='videoContainter']",
    "publication_date": "span.date::text, p.cat_time span.time::text",
    "author": "p.Normal strong::text, p.author_mail strong a::text, p.author span::text",
    "summary": "p.description::text, div.lead_detail::text",
}

DANTRI_SELECTORS = {
    "main_nav": "nav[role='navigation'] ol li a::attr(href)",
    "sub_nav": "nav[role='navigation'] ol li ol.submenu li a::attr(href)",
    "nav_folder": "ul.breadcrumbs li a::attr(href)",
    "category": "ul.breadcrumbs li a::attr(title)",
    "article": ".article-title a::attr(href)",
    "title": "h1.title-page::text",
    "content": "div.singular-content",
    "publication_date": "time.author-time::attr(datetime)",
    "author": "div.author-name a b::text",
    "summary": "h2.singular-sapo::text",
}

VNEXPRESS_CATEGORY_MAPPING = {
    "Menu-ThoiSu": "Thời sự",
    "Menu-TheGioi": "Thế giới",
    "Menu-KinhDoanh": "Kinh doanh",
    "Menu-GiaiTri": "Giải trí",
    "Menu-TheThao": "Thể thao",
    "Menu-PhapLuat": "Pháp luật",
    "Menu-GiaoDuc": "Giáo dục",
    "Menu-SucKhoe": "Sức khỏe",
    "Menu-DoiSong": "Đời sống",
    "Menu-DuLich": "Du lịch",
    "Menu-KhoaHoc": "Khoa học",
}

DANTRI_CATEGORY_MAPPING = {
    "Xã hội": "Thời sự",
    "Thế giới": "Thế giới",
    "Kinh doanh": "Kinh doanh",
    "Giải trí": "Giải trí",
    "Thể thao": "Thể thao",
    "Pháp luật": "Pháp luật",
    "Giáo dục - Hướng nghiệp": "Giáo dục",
    "Sức khỏe": "Sức khỏe",
    "An sinh": "Đời sống",
    "Văn hóa": "Du lịch",
    "Khoa học - Công nghệ": "Khoa học",
    "Bạn đọc": "Đời sống",
    "Sức mạnh số": "Khoa học",
    "Lao động - Việc làm": "Kinh doanh",
}

FALLBACK_CATEGORY = "Khác"

# Configure logging level
LOG_LEVEL = "INFO"
