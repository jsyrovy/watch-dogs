import requests

from dogs.dog import PriceDog


class DecathlonDog(PriceDog):
    SKU = ""
    URL = "https://www.decathlon.cz/cs/ajax/nfs/prices/online?skuIds="

    def _get_value(self) -> int:
        response = requests.get(f"{self.URL}{self.SKU}", timeout=5)
        response.raise_for_status()
        content: dict[str, dict[str, int]] = response.json()
        return content[self.SKU]["price"]
