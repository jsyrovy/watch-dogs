# pylint: disable=protected-access

import mock

from dogs.ikea.dog import IkeaDog


def test_get_value():
    class Response:
        text = '<span class="pip-temp-price__integer">1 234</span>'

    dog = IkeaDog()

    with mock.patch("dogs.ikea.dog.requests.get", return_value=Response()):
        assert dog._get_value() == 1234
