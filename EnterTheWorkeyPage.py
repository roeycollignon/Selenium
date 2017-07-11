from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(executable_path='C:/Selenium/chromedriver.exe')
driver.get('https://www.test.workey.co')

#button =  driver.find_element_by_class_name("btn btn-new-brand btn-lg margin-top-medium btn btn-default")
button =  driver.find_element_by_css_selector("button.btn.btn-new-brand.btn-lg.margin-top-medium.btn.btn-default")

print button.text
