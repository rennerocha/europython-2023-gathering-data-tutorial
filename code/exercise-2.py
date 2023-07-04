# Exercise 2

# Target: https://quotes.toscrape.com/scroll

# There has been another modification to the layout. Our quotes page
# now features an infinite scroll functionality, meaning that new
# content is dynamically loaded as you reach the bottom of the page.

# TIP: To understand this behavior, open your browser and access
# our target page. Press F12 to open the developer tools and
# select the "Network" tab. Observe what occurs in the network
# requests when you navigate to the end of the page.
import scrapy


class QuotesScrollSpider(scrapy.Spider):
    name = "quotes_scroll"
    allowed_domains = ["quotes.toscrape.com"]

    def start_requests(self):
        # TODO
        ...

    def parse(self, response):
        # TODO
        ...