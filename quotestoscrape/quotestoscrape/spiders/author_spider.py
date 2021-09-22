import scrapy

from ..items import AuthorItem


class AuthorSpider(scrapy.Spider):
    name = 'authors'
    start_urls = ['https://quotes.toscrape.com']

    def parse(self, response):
        for authors in response.css('.author + a::attr(href)'):
            yield response.follow(authors, callback=self.parse_author)

        next_page = response.css('li.next a::attr(href)').get()
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)

    def parse_author(self, response):
        item = AuthorItem()
        item['name'] = response.css('h3.author-title::text').get().strip()
        item['birthdate'] = response.css('span.author-born-date::text').get().strip()
        item['description'] = response.css('div.author-description::text').get().strip()
        yield item
