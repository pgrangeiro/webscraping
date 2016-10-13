# -*- coding: utf-8 -*-
import scrapy


class AuthorSpider(scrapy.Spider):
    name = "author"
    allowed_domains = ["quotes.toscrape.com"]
    start_urls = (
        'http://quotes.toscrape.com/',
    )

    def parse(self, response):
        paths = response.css('div.quote > span > a::attr(href)').extract()
        for path in paths:
            url = response.urljoin(path)
            yield scrapy.Request(url, callback=self.parse_author)

        next_page = response.css('li.next > a::attr(href)').extract_first()
        if next_page:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page)

    def parse_author(self, response):
        yield {
            'name': response.css('h3.author-title::text').extract_first().strip(),
            'born_at': response.css('span.author-born-date::text').extract_first().strip(),
        }
