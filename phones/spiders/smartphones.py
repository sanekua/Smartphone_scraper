# -*- coding: utf-8 -*-
import scrapy
import re
from ..items import PhonesItem


class SmartphonesSpider(scrapy.Spider):
    name = 'smartphones'
    allowed_domains = ['amazon.com']
    start_urls = ['https://www.amazon.com/b/ref=br_asw_smr?_encoding=UTF8&node=18637575011&pf_rd_m=ATVPDKIKX0DER&pf_rd_s=&pf_rd_r=6JQG5WK1NAEZ7MS8AGFJ&pf_rd_t=36701&pf_rd_p=74c2af8b-5acb-4bf8-b252-8b1584c94b14&pf_rd_i=desktop']

    def parse(self, response):
        items = PhonesItem()
        all_items = response.css('div.s-item-container')

        for respons in all_items:

            product_name = respons.css('.s-access-title').css('::text').extract()
            product_corp = respons.css('.a-color-secondary+ .a-color-secondary').css('::text').extract()
            product_price = respons.css('.a-color-base , .sx-price-whole').css('::text').extract()
            product_image = respons.css('.cfMarker::attr(src)').extract()


            items['product_name'] = product_name
            items['product_corp'] = product_corp
            items['product_price'] = (re.search(r'\d+',str(product_price)).group(0)).split()
            items['product_image'] = product_image

            yield items