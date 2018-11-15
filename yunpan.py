from selenium import webdriver
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Firefox()
driver.get('https://pan.baidu.com')
sleep(5)

driver.find_element_by_xpath('//*[@id="TANGRAM__PSP_4__footerULoginBtn"]').click()
driver.find_element_by_xpath('//*[@id="TANGRAM__PSP_4__userName"]').send_keys("13279552883")
driver.find_element_by_xpath('//*[@id="TANGRAM__PSP_4__password"]').send_keys("*****")
driver.find_element_by_xpath('//*[@id="TANGRAM__PSP_4__memberPass"]').click()
driver.find_element_by_xpath('//*[@id="TANGRAM__PSP_4__submit"]').click()


right_click = driver.find_element_by_xpath(".//*[@id='layoutMain']/div/div/div[2]/div/div/div[3]/div/div/dd[1]/div[2]/div[1]")

ActionChains(driver).context_click(right_click).perform()


