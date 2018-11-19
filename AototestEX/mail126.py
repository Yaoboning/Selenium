from selenium import webdriver



#login
def login():
    driver.find_element_by_id('idInput').clear()
    driver.find_element_by_id('idInput').send_keys('username')
    driver.find_element_by_id('pwdInput').clear()
    driver.find_element_by_id('pwdInput').send_keys('password')
    driver.find_element_by_id('loginBtn').click()


#logout
def logout():
    driver.find_element_by_link_text('退出').click()
    driver.quit()

driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.get("htps://www.126.com")

login()     #调用登录模块


logout()        #调用logout模块