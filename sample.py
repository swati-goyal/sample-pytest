import pytest
from assertpy import *
import requests as req


@pytest.mark.parametrize("x", [1, 0, 1, 2])
def test_xor(x):
    if x == 1:
        assert_that(x ^ 0).is_equal_to(1)
        assert_that(x ^ 1).is_equal_to(0)
    elif x == 0:
        assert_that(x ^ 1).is_equal_to(1)
        assert_that(x ^ 0).is_equal_to(0)
    else:
        print("Invalid input.")


def test_requests():
    res = req.get("https://google.com", params={'q': 'Quintype'})
    assert_that(res.status_code).is_equal_to(200)


