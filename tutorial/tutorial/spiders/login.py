# -*- coding: utf-8 -*-
import scrapy


class LoginSpider(scrapy.Spider):
    name = "login"
    allowed_domains = ["quotes.toscrape.com"]
    start_urls = (
        'http://quotes.toscrape.com/login',
    )

    def parse(self, response):
        token = response.css('input[name=csrf_token]::attr(value)').extract_first()
        yield scrapy.FormRequest(
            'http://quotes.toscrape.com/login',
            formdata={
                'username': 'xpto',
                'password': '1234',
                'csrf_token': token,
            },
            callback=self.parse_logged_in
        )

    def parse_logged_in(self, response):
        for quote in response.css('div.quote'):
            gt_url = quote.css('span > a:last-child::attr(href)')
            if gt_url:
                pass
