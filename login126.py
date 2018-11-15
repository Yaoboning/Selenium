from selenium import webdriver

driver = webdriver.Firefox()
driver.get("http://192.168.100.153:8088/login")
driver.maximize_window()
#title = webdriver.title
#print(title)


driver.find_element_by_xpath('html/body/div[2]/div/div/div[1]/ul/li[2]').click()
driver.find_element_by_xpath('html/body/div[2]/div/div/div[2]/div/form/div[1]/input').send_keys("zbceshi")
driver.find_element_by_xpath(".//*[@id='password']").send_keys('123456')
driver.find_element_by_xpath(".//*[@id='sub_enter']").click()
#title = webdriver.title
#print(title)
now_url =driver.current_url
print(now_url)

user =driver.find_element_by_xpath('//*[@id="logout"]').text
print(user)
driver.find_element_by_xpath(".//*[@id='logout']").click()


driver.find_element_by_xpath('html/body/div[2]/div/div/div[1]/ul/li[2]').click()
driver.find_element_by_xpath(".//*[@id='sub_gov2']").click()
driver.find_element_by_xpath(".//*[@id='enterQymc']").send_keys("山利科技")
driver.find_element_by_xpath(".//*[@id='enterQymc']").clear()
driver.find_element_by_xpath(".//*[@id='validation-form']/fieldset/div[9]/a").click()




driver.quit()


