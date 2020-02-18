# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

from scrapy.item  import Item,Field


class PlasticsItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()

    # Main Field
    main_headline = Field()
    headline = Field()

    # Separate Field
    url = Field()
    project = Field()
    spider = Field()
    server = Field()
    date = Field()

class TestItem(scrapy.Item):
    id = scrapy.Field()
    name = scrapy.Field()
    description = scrapy.Field()
