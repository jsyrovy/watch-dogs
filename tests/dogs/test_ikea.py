# pylint: disable=protected-access

import mock

from dogs.ikea.dog import IkeaDog


class TestDog(IkeaDog):
    URL = "https://www.ikea.com"
    NAME = "Product"
    PRICE = 1_000


def test_with_notification():
    value = 666
    dog = TestDog()

    with mock.patch.object(dog, "_get_value", return_value=value):
        assert dog._get_value() == value
        assert dog._should_send_notification(value) is True
        assert dog._get_notification_text(value) == f"<a href='{dog.URL}'>{dog.NAME}</a> je za {value}."


def test_without_notification():
    value = 10_000
    dog = TestDog()

    with mock.patch.object(dog, "_get_value", return_value=value):
        assert dog._get_value() == value
        assert dog._should_send_notification(value) is False


def test_get_value():
    value = 666

    class Response:
        text = f'<span class="pip-temp-price__integer">{value}</span>'

    dog = TestDog()

    with mock.patch("dogs.ikea.dog.requests.get", return_value=Response()):
        assert dog._get_value() == 666
