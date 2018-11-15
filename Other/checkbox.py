from selenium import webdriver
import os,time

driver = webdriver.Firefox()
file_path='file:///'+os.path.abspath('checkbox.html')
driver.get(file_path)

inputs=driver.find_element_by_tag_name('imput')

for i in inputs:
    if i.get_attribute('tepy')=='checkbox':
        i.click()
        time.sleep(1)
driver.quit()
