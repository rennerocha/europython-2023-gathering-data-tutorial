# Exercise 1

# Target: https://quotes.toscrape.com/

# On this page, you will find a collection of quotes along with their respective
# authors. Each quote is accompanied by a link that directs you to a dedicated
# page providing additional details about the author, the quote itself, and a list of associated tags.

# Your task is to extract all of this information and export it into a JSON lines file.

# TIP: your parse method can be used to yield items or schedule new requests for later processing.
import scrapy


class QuotesSpider(scrapy.Spider):
    name = "quotes"
    allowed_domains = ["quotes.toscrape.com"]
    start_urls = ["https://quotes.toscrape.com"]

    def parse(self, response):
        # TODO
        ...