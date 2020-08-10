#功能函数
import pytest


def multiply(a,b):
    return a * b
class TestMultiply:
    # =====Fixture=====
    @classmethod
    def setup_class(cls):                     #setup_class，teardown_class，在当前测试类的开始和结束时执行
        print("setup_class========>")

    @classmethod
    def teardown_class(cls):
        print("teardown_class=====>")

    def setup_method(self,method):            #setup_method，teardown_method，在每个测试方法的开始与结束时执行
        print("setup_method------->")

    def teardown_method(self,method):
        print("teardown_method---->")

    def setup(self):                         #setup，teardown，在每个测试方法的开始与结束时执行，可作用于测试函数
        print("setup-------------->")

    def teardown(self):
        print("teardown----------->")

#测试用例
    def test_numbers_5_6(self):
        if multiply(5,6)==19:
            print("哇哈哈")
        else:
            print('乐百氏')
        assert multiply(5, 6) == 30
    def test_strings_b_2(self):
        print('test_strings_b_2')
        assert multiply(3,2)== 7

if __name__ == '__main__':
    pytest.main()
    TestMultiply().test_numbers_5_6()
    TestMultiply().test_strings_b_2()