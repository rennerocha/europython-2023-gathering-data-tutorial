# Exercise 2

# Target: https://quotes.toscrape.com/js/

# The spider you created in the first exercise has ceased to function.
# Although no errors are evident in the logs, the spider is not returning any data.

# TIP: To troubleshoot, open your browser and navigate to our target page.
# Press Ctrl+U (View Page Source) to inspect the HTML content of the page.
import json
import scrapy


class QuotesJSSpider(scrapy.Spider):
    name = "quotes_js"
    allowed_domains = ["quotes.toscrape.com"]
    start_urls = ["https://quotes.toscrape.com/js/"]

    def parse(self, response):
        # TODO
        ...