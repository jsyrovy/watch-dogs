from utils.pushover import send_notification


class Dog:
    def run(self) -> None:
        value = self._get_value()
        print(f"{self.__class__.__name__}: {value=}")

        should_send_notification = self._should_send_notification(value)
        print(f"{self.__class__.__name__}: {should_send_notification=}")

        if should_send_notification:
            notification_text = self._get_notification_text(value)
            print(f"{self.__class__.__name__}: {notification_text=}")

            send_notification(notification_text)

    def _get_value(self) -> int:
        raise NotImplementedError

    def _should_send_notification(self, value: int) -> bool:
        raise NotImplementedError

    def _get_notification_text(self, value: int) -> str:
        raise NotImplementedError


class PriceDog(Dog):
    URL = ""
    NAME = ""
    PRICE = 0

    def _get_value(self) -> int:
        raise NotImplementedError

    def _should_send_notification(self, value: int) -> bool:
        return value < self.PRICE

    def _get_notification_text(self, value: int) -> str:
        text = f"<a href='{self.URL}'>{self.NAME}</a> je za {value}."
        print(text)
        return text
