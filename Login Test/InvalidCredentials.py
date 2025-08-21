import time
from selenium.webdriver.support.wait import WebDriverWait
from config import URL,Login_Invalid_Password,Login_Invalid_Username,Screenshot_Path
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

def test_with_Invalid_credentials():
    # Initialize the WebDriver with the modified options
    driver = webdriver.Chrome()
    # driver = webdriver.Chrome() # Open Chrome Browser
    try:
        driver.get(URL) # get to Open URL
        driver.find_element(By.ID,"username").send_keys(Login_Invalid_Username)
        driver.find_element(By.ID,"password").send_keys(Login_Invalid_Password)
        WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.CLASS_NAME,"radius"))).click()
        WebDriverWait(driver,20).until(EC.text_to_be_present_in_element((By.CLASS_NAME,"subheader"),"Welcome to the Secure Area. When you are done click logout below."))
        print("Your Code working fine")
        driver.save_screenshot(Screenshot_Path+"\\"+"login.png") #Enter Your Save Screenshot Path
    except Exception as e:
        print(f"Selenium Login Code Issue = {e}")
    finally:
        driver.quit()
