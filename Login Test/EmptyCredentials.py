from config import URL,Screenshot_Path
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

def empty_credentials():
    driver = webdriver.Chrome()
    try:
        driver.get(URL)
        print("----- Empty Credentials -----")
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, "radius"))).click()
        WebDriverWait(driver,20).until(EC.text_to_be_present_in_element((By.ID,"flash"),"Your username is invalid!"))
        driver.save_screenshot(Screenshot_Path+"\\"+"empty.png")
        print("Your Code working fine")
    except Exception as e:
        print(f"Selenium code have issue : {e}")

