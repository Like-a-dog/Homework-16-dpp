import pytest


def setup_module():
    print('setup:整个文件开始只在')


class TestClass():
    def setup_class(self):
        print('所有用例开始前执行')

    def teardown_class(self):
        print('所有用力执行后：执行')

    def test_print(self):
        print('测试用例已执行')
