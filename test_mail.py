from time import sleep
from selenium import webdriver
from module import Mail


driver = webdriver.Chrome()
driver.get("http://www.126.com")
# driver.get("http://www.163.com")

# 登录
# driver.switch_to.frame('x-URS-iframe')
# driver.find_element_by_name('email').clear()
# driver.find_element_by_name('email').send_keys('username')
# driver.find_element_by_name('password').clear()
# driver.find_element_by_name('password').send_keys('password')
# driver.find_element_by_id('dologin').clilk()
# sleep(5)
# driver.find_element_by_link_text("退出").click()
# driver.quit()

# 调用Mail类并接收driver驱动
mail = Mail(driver)
mail.login('1', '2')  # 登录
sleep(5)  # 登录之后的动作
mail.logout()  # 退出
driver.quit()
#
# driver = webdriver.Chrome()
# driver.get("http://www.126.com")
# mail = Mail(driver)
# mail.login(users[0][0], users[0][1])  # 登录
# sleep(5)  # 登录之后的动作
# mail.logout()  # 退出
# driver.quit()
