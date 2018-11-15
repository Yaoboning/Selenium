from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

driver = webdriver.Firefox()
driver.get('https://www.baidu.com')

driver.find_element_by_id('kw').send_keys("seleniumm")
sleep(2)
driver.find_element_by_id('kw').send_keys(Keys.BACK_SPACE)
print('1')
sleep(2)
driver.find_element_by_id('kw').send_keys(Keys.SPACE)
sleep(2)
driver.find_element_by_id('kw').send_keys("教程")
print('2')
sleep(2)
driver.find_element_by_id('kw').send_keys(Keys.CONTROL,'a')
sleep(2)
print('3')

driver.find_element_by_id('kw').send_keys(Keys.CONTROL,'x')
sleep(2)
print('4')

driver.find_element_by_id('kw').send_keys(Keys.CONTROL,'v')
sleep(2)
print('5')

driver.find_element_by_id('kw').send_keys(Keys.ENTER)
sleep(2)
print('6')

#driver.quit()
