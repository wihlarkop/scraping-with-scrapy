import scrapy

from ..items import QuoteItem


class QuotesSpider(scrapy.Spider):
    name = 'quotes'
    start_urls = ['https://quotes.toscrape.com']

    def parse(self, response):
        item = QuoteItem()

        quotes = response.css('div.quote')

        for quote in quotes:
            item['title'] = quote.css('span.text::text').get()
            item['author'] = quote.css('.author::text').get()
            item['tag'] = quote.css('a.tag::text').getall()

            yield item

        next_page = response.css('li.next a::attr(href)').get()
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)
