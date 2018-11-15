from selenium import webdriver

driver = webdriver.Firefox()
driver.get('https://www.youdao.com')

driver.find_element_by_id('border').send_keys("hello")
driver.find_element_by_id('border').submit()

driver.quit()
