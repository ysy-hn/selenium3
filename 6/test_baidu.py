import unittest
from time import sleep
from selenium import webdriver


# class TestBaidu(unittest.TestCase):
#
#     def setUp(self) -> None:
#         self.driver = webdriver.Chrome()
#         self.base_url = "https://www.baidu.com"
#
#     def test_search_key_selenium(self):
#         self.driver.get(self.base_url)
#         self.driver.find_element_by_id('kw').send_keys('selenium')
#         self.driver.find_element_by_id('su').click()
#         sleep(2)
#         title = self.driver.title
#         self.assertEqual(title, "selenium_百度搜索")
#
#     def test_search_key_unittest(self):
#         self.driver.get(self.base_url)
#         self.driver.find_element_by_id('kw').send_keys('unittest')
#         self.driver.find_element_by_id('su').click( )
#         sleep(2)
#         title = self.driver.title
#         self.assertEqual(title, "unittest_百度搜索")
#
#     def tearDowmn(self):
#         self.driver.quit()
#
#
# if __name__ == "__main__":
#     unittest.main()

# # 封装下，上面太繁琐
# class TestBaidu(unittest.TestCase):
#
#     def setUp(self) -> None:
#         print('测试开始')
#         self.driver = webdriver.Chrome()
#         self.base_url = "https://www.baidu.com"
#
#     def baidu_search(self, search_key):
#         self.driver.get(self.base_url)
#         self.driver.find_element_by_id('kw').send_keys(search_key)
#         self.driver.find_element_by_id('su').click()
#         sleep(2)
#
#     def test_search_key_selenium(self):
#         search_key = "selenium"
#         self.baidu_search(search_key)
#         self.assertEqual(self.driver.title, search_key + "_百度搜索")
#
#     def test_search_key_unittest(self):
#         search_key = "unittest"
#         self.baidu_search(search_key)
#         self.assertEqual(self.driver.title, search_key + "_百度搜索")
#
#     def tearDown(self):
#         print("测试结束")
#         self.driver.quit()
#
#
# if __name__ == '__main__':
#     unittest.main()


# 优化下，上面每次启动关闭用例，需要启动关闭浏览器，耗时
class TestBaidu(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        print('测试开始')
        cls.driver = webdriver.Chrome()
        cls.base_url = "https://www.baidu.com"

    def baidu_search(self, search_key):
        self.driver.get(self.base_url)
        self.driver.find_element_by_id('kw').send_keys(search_key)
        self.driver.find_element_by_id('su').click()
        sleep(2)

    def test_search_key_selenium(self):
        search_key = "selenium"
        self.baidu_search(search_key)
        self.assertEqual(self.driver.title, search_key + "_百度搜索")

    def test_search_key_unittest(self):
        search_key = "unittest"
        self.baidu_search(search_key)
        self.assertEqual(self.driver.title, search_key + "_百度搜索")

    @classmethod
    def tearDownClass(cls):
        print('测试结束')
        cls.driver.quit()


if __name__ == '__main__':
    unittest.main()

