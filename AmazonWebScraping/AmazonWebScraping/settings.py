# Scrapy settings for AmazonWebScraping project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = "AmazonWebScraping"

SPIDER_MODULES = ["AmazonWebScraping.spiders"]
NEWSPIDER_MODULE = "AmazonWebScraping.spiders"

# To store data explicitly or automatic while yield items
# FEEDS = {
#     'Amazon_Laptop_data.csv': {'format': 'csv'},
# }

SCRAPEOPS_API_KEY = '007bef54-1d27-466d-93d8-e5bd04349f45'
SCRAPEOPS_FAKE_USER_AGENT_ENDPOINT = 'https://headers.scrapeops.io/v1/user-agents'
SCRAPEOPS_FAKE_USER_AGENT_ENABLED = True
SCRAPEOPS_NUM_RESULTS = 50

SCRAPEOPS_FAKE_BROWSER_HEADER_ENDPOINT = 'https://headers.scrapeops.io/v1/browser-headers'
SCRAPEOPS_FAKE_BROWSER_HEADER_ENABLED = True

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = "AmazonWebScraping (+http://www.yourdomain.com)"

RETRY_HTTP_CODES = [500, 502, 503, 504, 522, 524, 408]
RETRY_TIMES = 3  # You can adjust the number of retry attempts
DOWNLOAD_DELAY = 3  # Add a 2-second delay between requests (you can adjust this)

# Obey robots.txt rules
ROBOTSTXT_OBEY = True

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
#DEFAULT_REQUEST_HEADERS = {
#    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
#    "Accept-Language": "en",
#}

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    "AmazonWebScraping.middlewares.AmazonwebscrapingSpiderMiddleware": 543,
#}

# place your proxy list to this
# ROTATING_PROXY_LIST = [
#     '191.209.43.16:5678',
#     '118.67.216.94:4145',
#     '103.60.137.17:4153'
# ]

# To take proxy from other file
# ROTATING_PROXY_LIST_PATH = 'J:\Amazon_Web_Scraping_Project\AmazonWebScraping\Proxies.txt'

# Rotating Proxies using ScrapeOps API
SCRAPEOPS_PROXY_ENABLED = True

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
    # "AmazonWebScraping.middlewares.ScrapeOpsFakeUserAgentMiddleware": 400,
    # "AmazonWebScraping.middlewares.ScrapeOpsFakeBrowserHeaderAgentMiddleware": 400,
    # "AmazonWebScraping.middlewares.AmazonwebscrapingDownloaderMiddleware": 543,

    # Use ScrapeOpsProxy Middleware to use
    "scrapeops_scrapy_proxy_sdk.scrapeops_scrapy_proxy_sdk.ScrapeOpsScrapyProxySdk": 725,

    # Using Scrapy Rotating proxies and ROTATING_PROXY_LIST
    # "rotating_proxies.middlewares.RotatingProxyMiddleware": 610,
    # "rotating_proxies.middlewares.BanDetectionMiddleware": 620,
}

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    "scrapy.extensions.telnet.TelnetConsole": None,
#}

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
   "AmazonWebScraping.pipelines.AmazonwebscrapingPipeline": 300,
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = "httpcache"
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = "scrapy.extensions.httpcache.FilesystemCacheStorage"

# Set settings whose default value is deprecated to a future-proof value
REQUEST_FINGERPRINTER_IMPLEMENTATION = "2.7"
TWISTED_REACTOR = "twisted.internet.asyncioreactor.AsyncioSelectorReactor"
# FEED_EXPORT_ENCODING = "utf-8"