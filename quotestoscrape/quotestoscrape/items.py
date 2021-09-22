from scrapy import Item, Field


class QuoteItem(Item):
    title = Field()
    author = Field()
    tag = Field()

class AuthorItem(Item):
    name = Field()
    birthdate = Field()
    description = Field()