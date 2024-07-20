from selenium import webdriver
import time

driver=webdriver.Chrome()

driver.get('https://www.zcool.com.cn/')
denlu=driver.find_element_by_link_text('登录')
denlu.click()
driver.close()