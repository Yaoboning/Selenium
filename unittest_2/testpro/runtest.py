import unittest

import testadd
import testsub

suit = unittest.TestSuite()

suit.addTest(testadd.TestAdd("test_add"))
suit.addTest(testadd.TestAdd("test_add2"))

suit.addTest(testsub.TestSub("test_sub"))
suit.addTest(testsub.TestSub("test_sub2"))

if __name__ =='__main__':

    runner = unittest.TextTestRunner()
    runner.run(suit)