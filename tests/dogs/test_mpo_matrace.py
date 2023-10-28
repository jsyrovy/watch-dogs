# pylint: disable=protected-access

import mock

from dogs.mpo_matrace.dog import MpoMatraceDog


def test_get_value():
    class Response:
        text = '<span class="price" id="our_price_display" itemprop="price">1 234 Kč</span>'

    dog = MpoMatraceDog()

    with mock.patch("dogs.mpo_matrace.dog.requests.get", return_value=Response()):
        assert dog._get_value() == 1234
