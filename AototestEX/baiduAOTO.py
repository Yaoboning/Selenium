from selenium import webdriver

search_text = ['python','chinese','text']

for text in search_text:
    driver =webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.get("https://www.baidu.com/")
    driver.find_element_by_id('kw').send_keys(text)
    driver.find_element_by_id('su').click()
    driver.get_screenshot_as_file('G://img.png')
    driver.quit()
