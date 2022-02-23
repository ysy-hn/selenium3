import unittest


class TestBdd(unittest.TestCase):

    def setUp(self):
        print("开始")

    def test_ccc(self):
        print('ccc')

    def test_aaa(self):
        print('aaa')


class TestAdd(unittest.TestCase):

    def setUp(self):   # setUp：测试开始动作
        print('开始')

    def tearDown(self):   # tearDown：测试结束动作
        print('结束')

    def test_bbb(self):
        print('bbb')

    def test_ddd(self):
        print('ddd')


if __name__ == "__main__":
    # unittest.main()
    suite = unittest.TestSuite()
    suite.addTest(TestBdd('test_aaa'))
    suite.addTest(TestBdd('test_ccc'))
    suite.addTest(TestAdd('test_bbb'))
    runner = unittest.TextTestRunner()
    runner.run(suite)
    # 在同一文件内，不能直接按顺序执行
