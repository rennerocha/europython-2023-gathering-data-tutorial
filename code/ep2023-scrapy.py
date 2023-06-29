import scrapy


class EuroPython2023Spider(scrapy.Spider):
    name = "europython"

    start_urls = [
        "https://ep2023.europython.eu/sessions",
        "https://ep2023.europython.eu/tutorials",
    ]

    def parse(self, response):
        for session in response.css("h2 a::text").getall():
            yield {"title": session}
