import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

dr = webdriver.Chrome()
dr.implicitly_wait(2)
wait = WebDriverWait(dr, 3)
dr.get('https://www.google.com.ua/')

el = dr.find_element(By.NAME, "q")
el.send_keys("Python")
# time.sleep(2)

#button = dr.find_element(By.XPATH, '//*[@id="tsf"]/div[2]/div[1]/div[2]/div[2]/div[2]/center/input[1]')
#time.sleep(2)
button = wait.until(
    EC.element_to_be_clickable((By.XPATH, '//*[@id="tsf"]/div[2]/div[1]/div[2]/div[2]/div[2]/center/input[1]')),
    message="Button search is not clickable"
)
print(button.text)
button.click()

links = wait.until(EC.presence_of_all_elements_located((By.PARTIAL_LINK_TEXT, "программирования")))
print(len(links))
for link in links:
    print(link.text)

#dr.quit()
#dr.close()