from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get('https://google.com')
print('nazwa strony',driver.title)
time.sleep(3)
button1_accept = driver.find_element('id', 'L2AGLb')
button1_accept.click()
print(button1_accept)
search_field = driver.find_element('name' , 'q')
search_field.send_keys('czy jutro jest niedzeia handlowa?')
search_button = driver.find_element("name" , "btnk")
search_button.submit()



time.sleep(2)

driver.quit()
