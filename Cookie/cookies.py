from selenium import  webdriver

driver = webdriver.Firefox()
driver.get("http://www.youdao.com")
d=driver.get_cookies()
print(d)

driver.add_cookie({'name':'key-aaaaaaa','value':'value-bbbbbbb'
                   })

for cookie in driver.get_cookies():
    print("%s -> %s" % (cookie['name'],cookie['value']))
driver.quit()