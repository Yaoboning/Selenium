class Login():


    def user_login(self,driver,username,password):
        driver.switch_to.frame('login_frame')
        driver.find_element_by_class_name('switch_btn_focus').click()
        #driver.find_element_by_xpath('//*[@id="uin_tips"]').clear()
        driver.find_element_by_xpath('//*[@id="uin_tips"]').send_keys('username')
       #driver.find_element_by_xpath('//*[@id="pwd_tips"]').clear()
        driver.find_element_by_xpath('//*[@id="pwd_tips"]').send_keys('password')
        driver.find_element_by_id('login_button').click()


    def user_logout(self,driver):
        driver.find_element_by_link_text('退出').click()
        driver.quit()


