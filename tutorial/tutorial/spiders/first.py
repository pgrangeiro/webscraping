# coding: utf-8

import scrapy


class FirstSpider(scrapy.Spider):

    # Todo spider tem que ter um nome
    name = 'First'

    def start_requests(self):
        # Tem que implementar um método responsável por fazer as requisições
        urls = [
            'http://quotes.toscrape.com/page/1/',
            'http://quotes.toscrape.com/page/2/',
        ]

        for url in urls:
            yield scrapy.Request(url, callback=self.parse)

    def parse(self, response):
        filename = '%s.html' % response.url.split('/')[-2]

        with open(filename, 'w') as f:
            f.write(response.text)
        self.log(u'Conteúdo da url %s salvo no arquivo %s' % (response.url, filename))
