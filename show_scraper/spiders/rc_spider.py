import scrapy

from show_scraper.items import Show
from show_scraper.loaders import ShowLoader
from show_scraper.settings import RC_START_URLS

class RcSpider(scrapy.Spider):
    name = "rc"
    allowed_domains = ["randomc.net"]
    start_urls = RC_START_URLS
    
    #xpaths
    showXpath = "//table[@id='season_preview']/tr[@id]"
    infoPrefix = ".//div[@class='preview_info']"
    titleXpath = infoPrefix + "/table/tr[1]/td/b/text()"
    descXpath = infoPrefix + "/table/tr[1]/td/text()"
    airdayXpath = infoPrefix + "/table/tr[3]/td[2]/text()"
    startdateXpath = infoPrefix + "/table/tr[2]/td[2]/text()"
    imageXpath = "./td[1]/img/@src"
    
    def parse(self, response):
        sel = scrapy.Selector(response)
        shows = sel.xpath(self.showXpath)
        items = []
        
        for show in shows:
            l = ShowLoader(Show(), show)
            l.add_xpath("id", self.titleXpath)
            l.add_xpath("title", self.titleXpath)
            l.add_xpath("desc", self.descXpath)
            l.add_xpath("airday", self.airdayXpath)
            l.add_xpath("startdate", self.startdateXpath)
            l.add_xpath("image_urls", self.imageXpath)
            items.append(l.load_item())
        
        return items
                
