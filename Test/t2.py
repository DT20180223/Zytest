#coding:utf-8

import time
from selenium import webdriver


driver = webdriver.Chrome()
driver.get("https://github.com/login")
driver.implicitly_wait(5)
driver.find_element_by_name("login").send_keys("3329001617@qq.com")
driver.find_element_by_name("password").send_keys("zy568521")
driver.find_element_by_name("commit").click()
time.sleep(3)

text = driver.find_element_by_css_selector(".dropdown-header.header-nav-current-user.css-truncate>.css-truncate-target").text
print("打印")
print(text)

driver.quit()