from selenium import webdriver
from time import sleep
class Login():


    def user_login(self,driver,username,password):
        iframe = driver.find_element_by_id("login_frame")
        driver.switch_to.frame('login_frame')
        driver.find_element_by_xpath(".//*[@id='switcher_plogin']").click()
        #driver.find_element_by_xpath('//*[@id="uin_tips"]').clear()
        driver.find_element_by_xpath(".//*[@id='u']").send_keys(username)
       #driver.find_element_by_xpath('//*[@id="pwd_tips"]').clear()
        driver.find_element_by_xpath(".//*[@id='p']").send_keys(password)
        driver.find_element_by_xpath(".//*[@id='login_button']").click()
        sleep(3)


    def user_logout(self,driver):
        #driver.find_element_by_link_text('退出').click()
        #driver.quit()


