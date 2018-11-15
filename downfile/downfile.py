from selenium import webdriver
import os

fp = webdriver.FirefoxProfile()

fp.set_preference("browser.download.folferList",2)
#设置为2，firefox保存文件到指定目录。0下载到浏览器默认路径。

fp.set_preference("browser.download.manager,shouWhenStarting",False)
#下载是否提示开始，Ture为显示，False为不显示。

fp.set_preference("browser.download.dir",os.getcwd())
#指定所下载文件的目录，os.getcwd（）函数不需要传递参数，用于返回当前目录。

fp.set_preference("browser.helperAPPs.neverAsk.saceToDisk","application/octet-stream")
#指定下载页面的Content-type值，“application/octet-stream”为文件类型。

driver = webdriver.Firefox(firefox_profile=fp)
driver.get("http://pypi.Python.org/pypi/selenium")
driver.find_element_by_partial_link_text("selenium-3").click()