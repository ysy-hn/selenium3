from selenium import webdriver

driver = webdriver.Chrome()
driver.get("http://www.baidu.com")

driver.find_element('id', 'kw').send_keys('selenium')
driver.find_element('id', 'su').click()
driver.quit()