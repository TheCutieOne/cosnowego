from selenium import webdriver
import time

driver = webdriver.Firefox()

driver.maximize_window()

driver.get("https://www.wsb.pl")

time.sleep(5)

driver.quit()
