from selenium import  webdriver

driver = webdriver.Firefox()
driver.get("http://192.168.100.153:8088")
d=driver.get_cookies()
print(d)

#driver.add_cookie({'name':'key-aaaaaaa','value':'value-bbbbbbb'})

for cookie in driver.get_cookies():
    print("%s -> %s" % (cookie['name'],cookie['value']))
driver.quit()