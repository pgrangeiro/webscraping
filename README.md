# Tutorial de Scrapy
Ministrado por @stummjr na #pybr12
https://github.com/stummjr/pybr12-tutorial/

## Resumo
- Obtendo dados úteis e estruturados
  - Nem sempre os dados estão dessa maneira na web

- Web Scraping
  - Pegar uma página HTML, por exemplo, e extrair os dados dela
- Web Crawling
  - Inclui automatização de navegação

- Utilizações
  - Monitoramento de preços

- Spiders
  - No Scrapy, são os crawlers em si

## Comandos
- Listar spiders
```sh
scrapy list
```

- Rodar spider
```sh
scrapy crawl _nome_spider_
```
- Inspecionar objetos da url a ser crawleada
```sh
scrapy shell _url_
```
Usando o Scrapy Shell para a url _http://quotes.toscrape.com/page/1/_ por exemplo:
```sh
>>> quote = response.css('div.quote')[0]
>>> authors = quote.css('small.author::text').extract()
>>> for author in authors: print(author)
```

## Ferramentas para extração
- No browser
  - Inspect do browser
    - Utilizado para descobrir a estrutura
  - Selector Gadget
- BeautifulSoup
- Scrapy Shell
