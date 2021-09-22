import scrapy


class AuthorSpider(scrapy.Spider):
    name = 'tags'
    start_urls = ['https://quotes.toscrape.com']

    def parse(self, response):
        for tags in response.css('span.tag-item a::attr(href)'):
            yield response.follow(tags, callback=self.parse)

            quotes = response.css('div.quote')

            for quote in quotes:
                item = [{
                    'title': quote.css('span.text::text').get(),
                    'author': quote.css('.author::text').get(),
                    'tag': quote.css('a.tag::text').getall(),
                }]

                yield {
                    'tag': response.css('h3 a::text').get(),
                    'quotes': item
                }

            next_page = response.css('li.next a::attr(href)').get()
            if next_page is not None:
                yield response.follow(next_page, callback=self.parse)
