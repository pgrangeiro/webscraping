# coding: utf-8

import scrapy


class FirstSpider(scrapy.Spider):

    # Todo spider tem que ter um nome
    name = 'First'

    # Se for usar o Request do próprio scrapy, basta apenas definir este attr com as uls a serem crawleadas
    start_urls = [
        'http://quotes.toscrape.com/page/1/',
        'http://quotes.toscrape.com/page/2/',
    ]

    def parse(self, response):
        filename = '%s.html' % response.url.split('/')[-2]

        with open(filename, 'w') as f:
            f.write(response.text)
        self.log(u'Conteúdo da url %s salvo no arquivo %s' % (response.url, filename))
