#coding: utf-8
import scrapy
from scrapy.crawler import CrawlerProcess


class amazon(scrapy.Spider):
    name = 'amazon'
    start_urls = []

    custom_settings = {
        'DOWNLOAD_DELAY': 0,
        'CONCURRENT_REQUESTS_PER_DOMAIN': 1,
        "FEEDS": {
            "amazon_books.json": {"format": "json"},
        }
    }

    def __init__(self):
        url = 'https://www.amazon.com.br/Administra%C3%A7%C3%A3o-Neg%C3%B3cios-e-Economia-Livros/s?rh=n%3A7872854011%2Cp_72%3A17833786011&page='

        for page in range(1, 100):
            self.start_urls.append(url + str(page))

    def parse(self, response):
        for livros in response.css('.a-size-medium'):
            yield {
                'titulo' : livros.css('.a-size-medium::text').get(),
                'precoDesconto' : response.css('.a-price:nth-child(1) span::text').get(),
                'preco' : response.css('.a-text-price span::text').get(),
                'author' : response.css('.a-color-secondary .a-size-base+ .a-size-base::text').get(),
                'quantidade_avaliacoes' : response.css('.s-link-style .s-underline-text::text').get()
            }

process = CrawlerProcess()
process.crawl(amazon)
process.start()