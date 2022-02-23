# # ！/usr/bin/python3
# -*- coding: utf-8 -*-
# 当前项目名称：python_基础教程
# 文件名称： unittest单元测试框架
# 登录用户名： yanshaoyou
# 作者： 闫少友
# 邮件： 2395969839@qq.com
# 电话：17855503800
# 创建时间： 2021/10/12  9:52

# import unittest
#
# class TestAssert(unittest.TestCase):
#
#     def test_equal(self):
#         self.assertEqual(2+2, 4)
#         self.assertEqual("python", "python")
#         self.assertNotEqual('hello', 'python')
#
#     def test_in(self):
#         self.assertIn("hello", "hello world")
#         self.assertNotIn('hi', "hello")
#
#     def test_true(self):
#         self.assertTrue(True)
#         self.assertFalse(False)
#
# if __name__ == "__main__":
#     unittest.main()

# import  unittest
# from Test_Bdd import *
#
# suite = unittest.TestSuite()
# suite.addTest(TestBdd('test_aaa'))
# suite.addTest(TestBdd('test_ccc'))
# suite.addTest(TestAdd('test_bbb'))
# runner = unittest.TextTestRunner()
# runner.run(suite)

import unittest
#
#
# class MyTest(unittest.TestCase):
#
#     @unittest.skip("直接跳过测试")
#     def test_skip(self):
#         print("aaa")
#
#     @unittest.skipIf(3 > 2, "当条件为真时跳过测试")
#     def test_skip_if(self):
#         print('bbb')
#
#     @unittest.skipUnless(3 > 2, '当条件为真时执行测试')
#     def test_skip_unless(self):
#         print('ccc')
#
#     @unittest.expectedFailure
#     def test_expected_failure(self):
#         self.assertEqual(2, 3)
#
#
# if __name__ == "__main__":
#     unittest.main()


# import unittest
#
#
# def setUpModule():
#     print("整个测试模块开始执行")
#
#
# def tearDownModule():
#     print('整个测试模块结束执行')
#
#
class MyTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("整个测试类开始执行，，需加装饰")

    @classmethod
    def tearDownClass(cls) -> None:
        print("整个测试类结束执行，需加装饰")

    def setUp(self):
        print("测试用例开始执行")

    # def tearDown(self) -> None:
    #     print("测试用例结束执行")

    def test_case1(self):
        print("测试1")

    def test_case2(self):
        print("测试2")


if __name__ == "__main__":
    unittest.main( )


