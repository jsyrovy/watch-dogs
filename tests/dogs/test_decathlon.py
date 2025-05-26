from unittest import mock

from dogs.decathlon.dog import DecathlonDog


def test_get_value():
    class Response:
        def json(self):
            return {"": {"price": 1234}}

        def raise_for_status(self): ...

    dog = DecathlonDog()

    with mock.patch("dogs.decathlon.dog.requests.get", return_value=Response()):
        assert dog._get_value() == 1234
