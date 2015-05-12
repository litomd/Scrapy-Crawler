# -*- coding: utf-8 -*-
import scrapy

from tslspyder.items import CancionItem

class AtmosferaSpider(scrapy.Spider):
    name = "atmosfera"
    allowed_domains = ["http://www.atmosfera.emisorasunidas.com/presionatmosferica"]
    start_urls = (
        'http://www.atmosfera.emisorasunidas.com/presionatmosferica/',
    )

    def parse(self, response):
        
         for sel in response.xpath('//div/div/div/div/div/ul/li/div/div'):
            item = CancionItem() 
            item['cancion'] = sel.xpath('p[contains(@class, "top-song")]/text()').extract().replace('^\d+\. ','');
            item['artista'] = sel.xpath('p[contains(@class, "top-autor")]/text()').extract();
            item['disco'] = sel.xpath('p[contains(@class, "top-disco")]/text()').extract();
            
            if item['cancion'] != '': 
                yield item 
