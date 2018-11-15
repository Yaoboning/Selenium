from selenium import webdriver
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Firefox()

driver.get("https://www.baidu.com")
sleep(2)


above = driver.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[3]/a[8]')
ActionChains(driver).move_to_element(above).perform()
