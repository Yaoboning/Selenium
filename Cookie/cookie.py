from selenium import webdriver

#get_cookies():
# 获得所有cookie

#get_cookie(name):
# 返回字典key为“name”的cookie信息

#add_cookie(cookie_dict):
# 添加 cookie “cookie_dict”指的是字典对象，必须有name和value。

#delete_cookie(name,optionsString):
# 删除cookie信息，“name”是要删除的cookie的名称，“optionsString”是该cookie的选项，目前支持的选项包括“路径”“域”。

#delete_all_cookies():
# 删除所有cookie信息。



driver = webdriver.Firefox()
driver.get("http://www.youdao.com")

#get cookie massage
cookie  = driver.get_cookies()
#print cookie massage
print(cookie)

driver.quit()