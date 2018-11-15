from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

driver =webdriver.Chrome()
driver.get('https://www.baidu.com')

link = driver.find_element_by_link_text('设置')
print(link)
ActionChains(driver).move_to_element(link).perform()

driver.find_element_by_link_text("搜索设置").click()

driver.find_element_by_class_name('prefpanelgo').click()

driver.switch_to.alert().accept()
#driver.quit()
