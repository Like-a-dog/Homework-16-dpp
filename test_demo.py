import pytest

"""
参数化：@pytest.mark.parametrize("变量名a",["对应变量的值value_a"],ids=["指明参数化对应的别名"])
"""


class TestDemo:
    @staticmethod
    def add(a, b):
        return a + b

    def test_ome(self):
        a = 5
        b = 1
        assert a == b

    @pytest.mark.parametrize("a, b, expected", [(3, 5, 2)], ids=["test_wrong_username"])
    def test_add(self, a, b, expected):
        assert self.add(a, b) == expected
