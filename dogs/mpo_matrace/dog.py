import requests
from bs4 import BeautifulSoup

from dogs.dog import PriceDog


class MpoMatraceDog(PriceDog):
    def _get_value(self) -> int:
        content = requests.get(self.URL, timeout=5).text
        soup = BeautifulSoup(content, "html.parser")
        return int(soup.find("span", id="our_price_display").text.replace("Kč", "").replace(" ", ""))
