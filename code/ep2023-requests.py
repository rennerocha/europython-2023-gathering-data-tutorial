import requests
from parsel import Selector


start_urls = [
    "https://ep2023.europython.eu/sessions",
    "https://ep2023.europython.eu/tutorials",
]
for url in start_urls:
    response = requests.get(url)
    content = Selector(text=response.text)

    for session in content.css("h2 a::text").getall():
        print(session)
