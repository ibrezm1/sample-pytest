

from unittest.mock import MagicMock
from unittest.mock import patch

from src.tdriver import testthis

import unittest

# mock from the local scope of the called function
# moch based on where it is used 
@patch('src.tdriver.mockthis')
def test_answer(mock_biz):
    mock_biz.return_value = "New val"
    print ('Returned : ' + testthis())
    assert 5 == 5

# content of test_class.py
class TestClass(unittest.TestCase):
    def test_one(self):
        x = "this"
        assert "h" in x

    def test_two(self):
        x = "hello"
        assert hasattr(x, "find")

    