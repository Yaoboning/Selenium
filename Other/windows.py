from selenium import webdriver
import time

driver =webdriver.Firefox()
driver.implicitly_wait(10)
driver.get("https://www.baidu.com")

sreach_windows =driver.current_window_handle
print(sreach_windows)
driver.find_element_by_xpath(".//*[@id='u1']/a[7]").click()
driver.find_element_by_link_text('立即注册').click()


all_handles = driver.window_handles
print(all_handles)
for handle in all_handles:
    if handle!=sreach_windows:
        driver.switch_to.window(handle)
        print('now register window!')
        driver.find_element_by_name("account").send_keys('username')
        driver.find_element_by_name("password").send_keys('password')
        time.sleep(2)


for handle in  all_handles:
    if  handle ==sreach_windows:
        driver.switch_to.window(handle)
        print('now sreach window!')
        second_widow = driver.current_window_handle

        driver.find_element_by_id('tangram__psp_4__closebtn').click()
        driver.find_element_by_id('kw').send_keys("selenium")
        driver.find_element_by_id('su').click()
        time.sleep(2)
print(all_handles)
#driver.quit()
