from selenium import webdriver
from public import Login


class LoginTest():

    def __init__(self):

        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.driver.get("https://mail.qq.com/cgi-bin/loginpage")

    def test_admin_login(self):
        username = '3253015738@qq.com'
        password = 'shanxishanli'
        Login().user_login(self.driver,username,password)



    def test_guest_login(self):
        username = '56545545'
        password = '45212213'
        Login().user_login(self.driver,username,password)
        #self.driver.quit()

LoginTest().test_admin_login()
LoginTest().test_guest_login()