from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time


driver = webdriver.Chrome("chromedriver.exe");
driver.get("https://srchostel.knust.edu.gh/#login")


error_text = 'Submission of applications for accomodation for SRC Hostel has ended.'

# submit = driver.find_element(By.CLASS_NAME, "btn-secondary")
# assert"Google" in driver.title
time.sleep(3)






switch = True
counter = 0 

while switch:
    username = driver.find_element(By.ID, 'usname')
    password = driver.find_element(By.ID, 'pwsd')
    form = driver.find_element(By.CLASS_NAME, 'form')

    username.send_keys("foagyei1")
    password.send_keys("3weyxd2")
    form.submit()

    lag = driver.find_element(By.CSS_SELECTOR, 'div.alert')
    if error_text in lag.get_attribute('innerHTML'):
        switch = True
        time.sleep(2)
        counter += counter 
        print(counter)
    else:
        switch = False
    



# 20856469
# easdjentuh


# easdjentuh
# 4fkonu4

# foagyei1
# 3weyxd2

