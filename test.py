from selenium import webdriver
from time import sleep
driver = webdriver.Chrome()
driver.get('http://www.baidu.com')
sleep(2)
kw = driver.find_element_by_id('kw');
kw.send_keys("chinese");
su = driver.find_element_by_id('su')
su.click()
