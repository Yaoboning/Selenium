from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()
driver.get("https://videojs.com/")

video = driver.find_element_by_xpath("body/Setion[1]/div/video")

url = driver.execute_script("return arguments[0].currentSrc;", video)
print(url)

print("start")
driver.execute_script("return arguments[0].play", video)

sleep(15)

print("stop")
driver.execute_script("arguments[0].pause()",video)

driver.quit()