from selenium import webdriver
import os

driver = webdriver.Firefox()
file_path = 'file:///'+os.path.abspath('upfile.html')
driver.get(file_path)

#定位上传按钮，添加本地文件
driver.find_element_by_name("file").send_keys('D:\\upload_file.txt')

driver.quit()