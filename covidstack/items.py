# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy.loader.processors import MapCompose, TakeFirst
from w3lib.html import remove_tags
import scrapy

def remove_html(value):
    value = value.replace("\u00a0", "").replace("\n", "").replace("&amp;", "&").replace("\u2013", "").replace("\u2019", "").replace("\u0020","")
    if value is not "":
        return value

class CovidCasesItem(scrapy.Item):

    country = scrapy.Field(
        input_processor = MapCompose(remove_tags, remove_html)
    )
    totalCases = scrapy.Field(
        input_processor = MapCompose(remove_tags)
    )
    newCases = scrapy.Field(
        input_processor = MapCompose(remove_tags, remove_html)
    )
    totalDeaths = scrapy.Field(
        input_processor = MapCompose(remove_tags, remove_html)
    )
    newDeaths = scrapy.Field(
        input_processor = MapCompose(remove_tags, remove_html)
    )
    totalRecovered = scrapy.Field(
        input_processor = MapCompose(remove_tags, remove_html)
    )
    activeCases = scrapy.Field(
        input_processor = MapCompose(remove_tags, remove_html)
    )
    critical = scrapy.Field(
        input_processor = MapCompose(remove_tags, remove_html)
    )
    total_cases_per_1M_pop = scrapy.Field(
        input_processor = MapCompose(remove_tags, remove_html)
    )
    deaths_per_1M_pop = scrapy.Field(
        input_processor = MapCompose(remove_tags, remove_html)
    )
    totalTests = scrapy.Field(
        input_processor = MapCompose(remove_tags, remove_html)
    )
    tests_per_1M_pop = scrapy.Field(
        input_processor = MapCompose(remove_tags, remove_html)
    )
