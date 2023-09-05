# pylint: disable=protected-access

import mock

from dogs import TrofastDog


def test_with_notification():
    value = 666
    dog = TrofastDog()

    with mock.patch.object(dog, "_get_value", return_value=value):
        assert dog._get_value() == value
        assert dog._should_send_notification(value) is True
        assert dog._get_notification_text(value) == f"<a href='{dog.URL}'>Trofast</a> je za {value}."


def test_without_notification():
    value = 10_000
    dog = TrofastDog()

    with mock.patch.object(dog, "_get_value", return_value=value):
        assert dog._get_value() == value
        assert dog._should_send_notification(value) is False


def test_get_value():
    value = 666

    class Response:
        text = f'<span class="pip-temp-price__integer">{value}</span>'

    dog = TrofastDog()

    with mock.patch("dogs.ikea_trofast.requests.get", return_value=Response()):
        assert dog._get_value() == 666
