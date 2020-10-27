import time

import self as self
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



dr = webdriver.Chrome()
dr.maximize_window()
actions = webdriver.ActionChains(dr)
#dr.get('https://www-archive.mozilla.org/projects/ui/accessibility/unix/testcase/html/')
dr.get('https://www.python.org/')

'''DropDownMenu'''
# dropdown = dr.find_element(By.ID, 'options')
# dropdown.click()
# dropdown.find_element(By.XPATH, '//*[@id="options"]/option[7]')
# time.sleep(3)
# dropdown.click()
# time.sleep(3)

'''DropDownMenu2'''
# dropdown = Select(dr.find_element(By.ID, 'options'))
# time.sleep(3)
# dropdown.select_by_value('href')
# time.sleep(3)

'''RadioButton'''
# radiobutton = dr.find_element(By.XPATH, '//*[@id="rbutton3"]')
# time.sleep(3)
# radiobutton.click()
# time.sleep(3)

'''CheckBox ??'''
# element = dr.find_elements(By.ID, 'ch1')
# if element.is_selected():
#     print('Check box is already selected')
# else:
#     element.click()

'''ActionChains'''
button = dr.find_element(By.XPATH, '//*[@id="downloads"]/a')
sub_button = dr.find_element(By.XPATH, '//*[@id="downloads"]/ul/li[3]/a')

actions.move_to_element(button)
actions.move_to_element(sub_button)
actions.click()
actions.perform()

#dr.close()