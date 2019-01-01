import unittest

def setUpModule():
    print("test model start >>>>>>>>>>>>>>>>>>>>>>")

def tearDownModule():
    print("test model  end  >>>>>>>>>>>>>>>>>>>>>")

class test (unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("test class start =========>>>>>>>>")

    @classmethod
    def tearDownClass(cls):
        print("test class end ==========>>>>>>>>>")

    def setUp(self):
        print("test case start  --->>>>")

    def tearDown(self):
        print("test case end  --->>>>>>")

    def test_case(self):
        print("test case1")
    def test_case2(self):
        print("test case2")

if  __name__ =='__main__':
    unittest.main()

    # setUpModule/tearDowmModule :          在整个模块的开始与结束执行
    # setUpClass/tearDownClass  :           在测试类的开始与结束执行
    # setUp/tearDown    :                   在测试用例的开始与结束执行
# setUpClass/tearDownClass  :    的写法稍有不同，首先需要通过@classmethod进行装饰，其次使用方法的参数是cls