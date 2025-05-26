import requests

from dogs.dog import PriceDog


class DecathlonDog(PriceDog):
    SKU = ""
    URL = "https://www.decathlon.cz/cs/ajax/nfs/prices/online?skuIds="

    def _get_value(self) -> int:
        headers = {
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36",  # noqa: E501
        }
        response = requests.get(f"{self.URL}{self.SKU}", timeout=5, headers=headers)
        response.raise_for_status()
        content: dict[str, dict[str, int]] = response.json()
        return content[self.SKU]["price"]
