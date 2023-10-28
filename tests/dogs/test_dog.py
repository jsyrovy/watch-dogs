# pylint: disable=protected-access

import mock
import pytest

from dogs.dog import Dog, PriceDog


class TestDog(Dog):
    def __init__(self, send_notification):
        self._send_notification = send_notification

    def _get_value(self):
        return 0

    def _should_send_notification(self, value):
        return self._send_notification

    def _get_notification_text(self, value):
        return "test"


class TestPriceDog(PriceDog):
    URL = "https://www.web.com"
    NAME = "Product"
    PRICE = 1_000

    def _get_value(self):
        return 0


def test_run_without_notification():
    dog = TestDog(send_notification=False)

    with mock.patch("dogs.dog.send_notification") as send_notification_mock:
        dog.run()

    send_notification_mock.assert_not_called()


def test_run_with_notification():
    dog = TestDog(send_notification=True)

    with mock.patch("dogs.dog.send_notification") as send_notification_mock:
        dog.run()

    send_notification_mock.assert_called_once_with("test")


def test_base_dog():
    dog = Dog()

    with pytest.raises(NotImplementedError):
        dog._get_value()

    with pytest.raises(NotImplementedError):
        dog._should_send_notification(None)

    with pytest.raises(NotImplementedError):
        dog._get_notification_text(None)


def test_price_dog_with_notification():
    value = 666
    dog = TestPriceDog()

    with mock.patch.object(dog, "_get_value", return_value=value):
        assert dog._get_value() == value
        assert dog._should_send_notification(value) is True
        assert dog._get_notification_text(value) == f"<a href='{dog.URL}'>{dog.NAME}</a> je za {value}."


def test_price_dog_without_notification():
    value = 10_000
    dog = TestPriceDog()

    with mock.patch.object(dog, "_get_value", return_value=value):
        assert dog._get_value() == value
        assert dog._should_send_notification(value) is False
