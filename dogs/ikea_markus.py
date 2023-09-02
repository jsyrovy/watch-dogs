import requests
from bs4 import BeautifulSoup

from dogs.dog import Dog


class MarkusDog(Dog):
    URL = "https://www.ikea.com/cz/cs/p/markus-kancelarska-zidle-vissle-tmave-seda-70261150"

    def _get_value(self) -> int:
        content = requests.get(self.URL, timeout=5).text
        soup = BeautifulSoup(content, "html.parser")
        return int(soup.find("span", class_="pip-temp-price__integer").text.replace(" ", ""))

    def _should_send_notification(self, value: int) -> bool:
        return value < 4000

    def _get_notification_text(self, value: int) -> str:
        text = f"<a href='{self.URL}'>Markus</a> je za {value}."
        print(text)
        return text
