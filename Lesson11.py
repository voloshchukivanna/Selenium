from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

dr = webdriver.Chrome()
# actions = webdriver.ActionChains(dr)
dr.get("http://127.0.0.1:88/oxwall/")

# def is_button_present():

sign_in = dr.find_element(By.CLASS_NAME, 'ow_signin_label')
sign_in.click()

email = dr.find_element(By.NAME, 'identity')
email.clear()
email.send_keys('admin')

password = dr.find_element(By.NAME, 'password')
password.clear()
password.send_keys('pass')

button_sign_in = dr.find_element(By.NAME, 'submit')
button_sign_in.click()

time.sleep(5)

