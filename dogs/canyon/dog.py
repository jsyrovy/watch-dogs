import requests
from bs4 import BeautifulSoup

from dogs.dog import PriceDog


class CanyonDog(PriceDog):
    def _get_value(self) -> int:
        content = requests.get(self.URL, timeout=5).text
        soup = BeautifulSoup(content, "html.parser")
        if not (price_element := soup.find("div", class_="productDescription__priceSale")):
            raise ValueError("Price element not found")
        return int(price_element.text.replace("CZK", "").replace(".", "").replace(" ", ""))
