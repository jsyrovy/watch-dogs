# pylint: disable=protected-access

import mock
import pytest

from dogs.dog import Dog


class TestDog(Dog):
    def __init__(self, send_notification):
        self._send_notification = send_notification

    def _get_value(self):
        return 0

    def _should_send_notification(self, value):
        return self._send_notification

    def _get_notification_text(self, value):
        return "test"


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
