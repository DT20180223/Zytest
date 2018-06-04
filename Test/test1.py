from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time
import sys
print(sys.path)
# driver =webdriver.Firefox()
driver = webdriver.Chrome()
driver.get("https://mail.163.com/")
time.sleep(2)
iframe = driver.find_element_by_id("x-URS-iframe")
driver.switch_to.frame(iframe)
# driver.find_element_by_class_name("j-inputtext dlemail").send_keys("zhaoyao1989")
#
# driver.find_element_by_class_name("j-inputtext dlpwd").send_keys("zhaoyao_1989")
driver.find_element_by_name("email").send_keys("123")

driver.find_element_by_name("password").send_keys("456")

driver.find_element_by_class_name("u-loginbtn btncolor tabfocus btndisabled").click()




# time.sleep(2)
# h = driver.current_window_handle
# print(h)
# driver.find_element_by_link_text("返回金石基金").click()
# time.sleep(3)
# all_h = driver.window_handles
# print(all_h)
#
# driver.switch_to.window(all_h[1])
#
# print(driver.title)




# mouse = driver.find_element_by_link_text("设置")
# ActionChains(driver).move_to_element(mouse).perform()
# time.sleep(1)
# ActionChains(driver).context_click()
# driver.find_element_by_id("kw").send_keys("python")
# driver.find_element_by_name("wd").send_keys("python")
# driver.find_element_by_tag_name("input").send_keys("python")
# driver.find_element_by_link_text("hao123").click()
# driver.find_element_by_xpath(".//*[@id='kw']").send_keys("python")
# driver.find_element_by_class_name("btn self-btn bg s_btn").click()
# driver.set_window_size(540,960)
# driver.find_element_by_css_selector("#kw").send_keys(u"测试部落")
# time.sleep(3)
# driver.find_element_by_css_selector("#kw").clear()
# driver.find_element_by_css_selector("#kw").send_keys(Keys.F1)
# driver.find_element_by_css_selector("#kw").submit()

# driver.get("https://www.hordehome.com"
time.sleep(3)



# s = driver.find_elements_by_css_selector("h3.t>a")

# for i in s:
#     print(i.get_attribute("href"))
# driver.get_screenshot_as_file("F:\PycharmProjects\Open_API\Test\\2.png")
# driver.back()
# time.sleep(3)
# driver.forward()
driver.close()
driver.quit()