# import csv
# import codecs
# import unittest
# from time import sleep
# from itertools import islice
# from selenium import webdriver
#
#
# class TestBaidu(unittest.TestCase):
#
#     @classmethod
#     def setUpClass(cls) -> None:
#         cls.driver = webdriver.Chrome()
#         cls.base_url = "https://www.baidu.com"
#
#     @classmethod
#     def tearDownClass(cls) -> None:
#         cls.driver.quit()
#
#     def baidu_search(self, search_key):
#         self.driver.get(self.base_url)
#         self.driver.find_element_by_id('kw').send_keys(search_key)
#         self.driver.find_element_by_id('su').click()
#         sleep(3)
#
#     def test_search(self):
#         with codecs.open('baidu_data.csv', 'r', 'utf-8-sig') as f:
#             data = csv.reader(f)
#             for line in islice(data, 1, None):
#                 search_key = line[1]
#                 self.baidu_search(search_key)
#
# if __name__ == '__main__':
#     unittest.main(verbosity = 2)


# 优化，上面的for循环会导致失败情况不明确
import csv
import codecs
import unittest
from time import sleep
from itertools import islice
from selenium import webdriver


class TestBaidu(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = webdriver.Chrome()
        cls.base_url = "https://www.baidu.com"
        cls.test_data = []
        with codecs.open('baidu_data.csv', 'r', 'utf-8-sig') as f:
            data = csv.reader(f)
            for line in islice(data, 1, None):
                cls.test_data.append(line)

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()

    def baidu_search(self, search_key):
        self.driver.get(self.base_url)
        self.driver.find_element_by_id('kw').send_keys(search_key)
        self.driver.find_element_by_id('su').click()
        sleep(3)

    def test_search_selenium(self):
        self.baidu_search(self.test_data[0][1])

    def test_search_unittest(self):
        self.baidu_search(self.test_data[1][1])


if __name__ == '__main__':
    unittest.main(verbosity = 2)
