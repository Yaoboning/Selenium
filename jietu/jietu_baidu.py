from selenium import  webdriver
from  time import sleep

driver = webdriver.Chrome()
driver.get("https://www.baidu.com")

driver.find_element_by_id('kw').send_keys('selenium')
driver.find_element_by_id('su').click()
sleep(2)
driver.get_screenshot_as_file("G:\\baiduimg.png")
driver.quit()