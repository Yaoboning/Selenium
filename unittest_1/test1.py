from Tools.scripts.which import msg

from calculator import Count
import unittest

class TestCount(unittest.TestCase):
    def setUp(self):
        print("test start")

    def test_add(self):
        j = Count(2,3)
        self.assertEqual(j.add(),5)

    def test_add2(self):
        j = Count(41,76)
        self.assertEqual(j.add(),117)

    def tearDown(self):
        print("test end")

if __name__ == '__main__':

    suite = unittest.TestSuite()
    suite.addTest(TestCount("test_add2"))

    runner = unittest.TextTestRunner()
    runner.run(suite)

# unittest框架的TestCase类提供以下这些方法用于测试结果的判断。
# assertEqual(a,b,msg)      判断a，b 。msg为可选参数，用于定义测试失败时打印消息。
# 方法                                检查
# assertEqual(a,b)                      a==b
# assertNotEqual(a,b)                    a!=b
# assertTrue(x)                         bool(x)is True
# sssertFalse(x)                         bool(x)is False
# assertIs(a,b)                          a is b
# assertNot(a,b)                        a is not b
# assertIn(a,b)                         a in b
# assertNotIn(a,b)                      a not in b
# assertIsInstance(a,b)                 isinstance(a,b)
# assertNotIsInstance(a,b)               not isinstance(a,b)
# isinstance()语法    isinstance(object,classinfo)
        # object 实例对象。
        # classinfo 可以是之间或间接类名、基本类型或者由他们组成的元素。
        # 对于基本的类型来说classinfo可以是：int,float,bool,complex,str,list,dict,set,tuple.
        # 如果对象的类型和classinfo对象类型相同则返回True，否则返回False。