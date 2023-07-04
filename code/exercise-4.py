import scrapy


class QuotesViewStateSpider(scrapy.Spider):
    name = "quotes_viewstate"
    allowed_domains = ["quotes.toscrape.com"]
    start_urls = ["http://quotes.toscrape.com/search.aspx"]

    def parse(self, response):
        authors = response.css("#author option::attr(value)").getall()

        form_data = {
            # TODO
        }
        for author in authors:
            yield scrapy.FormRequest(
                response.urljoin(response.css("form::attr(action)").get()),
                callback=self.parse_author_tags,
                formdata=form_data,
                cb_kwargs={"author": author}
            )

    def parse_author_tags(self, response, author):
        # TODO
        ...