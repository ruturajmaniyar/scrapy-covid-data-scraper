from scrapy.loader import ItemLoader
from covidstack.items import CovidCasesItem
import scrapy

class CovidstackSpider(scrapy.Spider):
    name = 'covidstack'
    start_urls = ['https://www.worldometers.info/coronavirus/']

    def parse(self, response): 
        for item in response.xpath("//table/tbody/tr"):
            l = ItemLoader(item=CovidCasesItem(), selector=item)
            l.add_xpath('country','.//td[1]/a')
            l.add_xpath('totalCases', './/td[2]')
            l.add_xpath('newCases', './/td[3]')
            l.add_xpath('totalDeaths', './/td[4]')
            l.add_xpath('newDeaths', './/td[5]')
            l.add_xpath('totalRecovered', './/td[6]')
            l.add_xpath('activeCases', './/td[7]')
            l.add_xpath('critical', './/td[8]')
            l.add_xpath('total_cases_per_1M_pop', './/td[9]')
            l.add_xpath('deaths_per_1M_pop', './/td[10]')
            l.add_xpath('totalTests', './/td[11]')
            l.add_xpath('tests_per_1M_pop', './/td[12]')
            yield l.load_item()
