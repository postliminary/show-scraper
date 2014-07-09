# -*- coding: utf-8 -*-

# Scrapy settings for show_scraper project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'show_scraper'

SPIDER_MODULES = ['show_scraper.spiders']
NEWSPIDER_MODULE = 'show_scraper.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'show_scraper (+http://www.yourdomain.com)'

#File Output
FEED_STORAGES = { 'owfile': 'show_scraper.feedexport.OverwriteFileFeedStorage' }
FEED_URI = 'owfile:./output/shows.json'
FEED_FORMAT = 'json'

#Item Pipeline
ITEM_PIPELINES = {
        'scrapy.contrib.pipeline.images.ImagesPipeline': 10
    }
    
#Image Path
IMAGES_STORE = './output/images'

#RC Spider Urls
RC_START_URLS = [
    "http://randomc.net/2014/03/27/spring-2014-preview/",
    "http://randomc.net/2014/06/18/summer-2014-preview/"
]
