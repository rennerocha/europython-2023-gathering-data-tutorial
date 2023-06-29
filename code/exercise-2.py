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
    api_url = "https://quotes.toscrape.com/api/quotes?page={page}"

    def start_requests(self):
        yield scrapy.Request(self.api_url.format(page=1))

    def parse(self, response):
        data = response.json()
        actual_page = data.get("page")

        for quote in data.get("quotes"):
            yield {
                "quote": quote.get("text"),
                "author": quote.get("author").get("name"),
                "author_url": response.urljoin(
                    quote.get("author").get("goodreads_link")
                ),
                "tags": quote.get("tags"),
            }

        if data.get("has_next"):
            next_page = actual_page + 1
            yield scrapy.Request(
                self.api_url.format(page=next_page),
            )
