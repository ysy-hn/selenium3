import unittest
from time import sleep
from selenium import webdriver
from baidu_page import BaiduPage


class TestBaidu(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = webdriver.Chrome()

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()

    def test_baidu_search_case1(self):
        page = BaiduPage(self.driver)
        page.open()
        page.search_input('selenium')
        sleep(2)
        self.assertEqual(page.get_title(), "selenium_百度搜索")

    def test_baidu_search_case2(self):
        page = BaiduPage(self.driver)
        page.get("https://www.baidu.com")
        page.search_input = 'selsnium'
        page.search_button.click()


if __name__ == '__main__':
    unittest.main(verbosity = 2)

