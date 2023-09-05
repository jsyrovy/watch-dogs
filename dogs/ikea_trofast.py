import requests
from bs4 import BeautifulSoup

from dogs.dog import Dog


class TrofastDog(Dog):
    URL = "https://www.ikea.com/cz/cs/p/trofast-ulozna-sestava-svetle-morena-borovice-bila-s89102095"

    def _get_value(self) -> int:
        content = requests.get(self.URL, timeout=5).text
        soup = BeautifulSoup(content, "html.parser")
        return int(soup.find("span", class_="pip-temp-price__integer").text.replace(" ", ""))

    def _should_send_notification(self, value: int) -> bool:
        return value < 3800

    def _get_notification_text(self, value: int) -> str:
        text = f"<a href='{self.URL}'>Trofast</a> je za {value}."
        print(text)
        return text
