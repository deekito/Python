import selenium.webdriver
from time import sleep

driver = selenium.webdriver.Chrome()

driver.maximize_window()

driver.get('http://www.google.com')

sleep(5)

driver.find_element_by_id('kw').send_keys('Python for Selenium')

driver.find_element_by_id('su').click()

sleep(5)

driver.quit()

