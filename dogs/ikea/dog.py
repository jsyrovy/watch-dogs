import requests
from bs4 import BeautifulSoup

from dogs.dog import PriceDog


class IkeaDog(PriceDog):
    def _get_value(self) -> int:
        content = requests.get(self.URL, timeout=5).text
        soup = BeautifulSoup(content, "html.parser")
        return int(soup.find("span", class_="pip-temp-price__integer").text.replace(" ", ""))
