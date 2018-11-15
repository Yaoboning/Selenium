#execute_script()
#window.scrollTo(0,450) #(左边距，上边距)

from selenium import webdriver
from time import sleep

driver = webdriver.Firefox()
driver.get("http://www.baidu.com")

driver.set_window_size(800,600)

driver.find_element_by_id("kw").send_keys("selenium")
driver.find_element_by_id("su").click()
sleep(2)

js="window.scrollTo(100,100);"
driver.execute_script(js)
sleep(3)


driver.quit()