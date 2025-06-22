from unittest import mock

from dogs.canyon.dog import CanyonDog


def test_get_value():
    class Response:
        text = '<div class="productDescription__priceSale"> 1.234 CZK </div>'

    dog = CanyonDog()

    with mock.patch("dogs.ikea.dog.requests.get", return_value=Response()):
        assert dog._get_value() == 1234
