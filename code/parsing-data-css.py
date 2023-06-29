import scrapy


class EuroPython2023Spider(scrapy.Spider):
    name = "europython"

    start_urls = [
        "https://ep2023.europython.eu/sessions",
        "https://ep2023.europython.eu/tutorials",
    ]

    def parse(self, response):
        sessions = response.css(".mt-12")
        for session in sessions:
            yield {
                "title": session.css("h2 a::text").get(),
                "presenter": session.css("p a::text").get(),
            }
