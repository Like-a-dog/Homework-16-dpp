import logging

import pytest
from Common.Calculator import Calculation


class TestCalc:
    def setup_class(self):
        print('开始计算')

    def teardown_class(self):
        print('计算结束')

    @pytest.mark.parametrize("a,b,expect", [(1, 2, 3)])
    def test_add(self, a, b, expect):
        assert Calculation().add(a, b) == expect

    @pytest.mark.parametrize("a,b,expect", [(1, 2, -1)])
    def test_reduce(self, a, b, expect):
        assert Calculation().reduce(a, b) == expect

    @pytest.mark.parametrize("a,b,expect", [(1, 2, 2)])
    def test_ride(self, a, b, expect):
        assert Calculation().ride(a, b) == expect

    @pytest.mark.parametrize("a,b,expect", [(1, 2, 2)])
    def test_division(self, a, b, expect):
        assert Calculation().division(a, b) == expect
