from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time


driver = webdriver.Chrome("chromedriver.exe");
driver.get("https://gusss.knust.edu.gh/booking")
username = driver.find_element(By.ID, 'email')
password = driver.find_element(By.ID, 'pwd')
form = driver.find_element(By.ID, 'login_frm')
# submit = driver.find_element(By.CLASS_NAME, "btn-secondary")
# assert"Google" in driver.title

x = 0

while x !=1:
#      easdjentuh
# 4fkonu4

# foagyei1
# 3weyxd2
    username.send_keys("foagyei1")
    password.send_keys("3weyxd2")
    form.submit()
    time.sleep(7)
    current_url = driver.current_url
    alert = driver.find_element(By.CLASS_NAME, 'alert')
    print(alert)
    if alert == "":
        x = 1


# 20856469
# easdjentuh
# submit.click()

