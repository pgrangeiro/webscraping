# coding: utf-8

import scrapy


class SecondSpider(scrapy.Spider):
    '''
        scrapy crawl Second -o test.json
    '''

    name = 'Second'
    start_urls = [
        'http://quotes.toscrape.com',
    ]

    def parse(self, response):
        for quote in response.css('div.quote'):
            yield {
                'quote': quote.css('span.text::text').extract_first(),
                'author': quote.css('span > small.author::text').extract_first(),
                'tag': quote.css('a.tag::text').extract(),
            }

        next_page = response.css('li.next > a::attr(href)').extract_first()
        if next_page:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page)
