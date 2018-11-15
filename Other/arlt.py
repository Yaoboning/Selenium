#coding=utf-8
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time

driver = webdriver.Firefox()
driver.implicitly_wait(10)
driver.get ('https://www.baidu.com')

above = driver.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[3]/a[8]')
ActionChains(driver).move_to_element(above).perform()


driver.find_element_by_class_name('setpref').click()

driver.find_element_by_class_name("prefpanelgo").click()
time.sleep(2)

driver.switch_to_alert().accept()
driver.quit()