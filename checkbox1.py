from selenium import webdriver
import os,time
from time import sleep

driver =webdriver.Firefox()
driver.get('http://192.168.100.153:8088/login')

driver.find_element_by_xpath('html/body/div[2]/div/div/div[1]/ul/li[2]').click()
driver.find_element_by_xpath('html/body/div[2]/div/div/div[2]/div/form/div[1]/input').send_keys("gxceshi")
driver.find_element_by_xpath(".//*[@id='password']").send_keys('123456')
driver.find_element_by_xpath(".//*[@id='sub_enter']").click()
driver.find_element_by_xpath('//*[@id="userControl"]/li[3]/a').click()
driver.find_element_by_xpath('//*[@id="sidebar"]/ul/li[3]/a/span').click()
driver.find_element_by_xpath('//*[@id="submenud402ce37-d6d0-4d53-bcfe-c71346371939"]/li[2]/a/span').click()
sleep(1)

iframe=driver.find_element_by_id('mainFrame')
driver.switch_to.frame(iframe)
driver.find_element_by_xpath(".//*[@id='table']/tbody/tr[2]/td[5]/a[1]").click()


checkboxes = driver.find_elements_by_xpath("//input[@type='checkbox']")

for checkbox in checkboxes:
    checkbox.click()
    time.sleep(1)

print(len(checkboxes))
driver.find_elements_by_css_selector('input[type=checkbox]').pop().click()
driver.quit()
