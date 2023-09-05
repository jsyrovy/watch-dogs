import requests
from bs4 import BeautifulSoup

from dogs.dog import Dog


class LaettDog(Dog):
    URL = "https://www.ikea.com/cz/cs/p/laett-detsky-stul-a-2-zidle-bila-borovice-50178411"

    def _get_value(self) -> int:
        content = requests.get(self.URL, timeout=5).text
        soup = BeautifulSoup(content, "html.parser")
        return int(soup.find("span", class_="pip-temp-price__integer").text.replace(" ", ""))

    def _should_send_notification(self, value: int) -> bool:
        return value < 900

    def _get_notification_text(self, value: int) -> str:
        text = f"<a href='{self.URL}'>Lätt</a> je za {value}."
        print(text)
        return text
