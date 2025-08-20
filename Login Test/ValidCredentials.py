from config import URL,Login_Username,Login_Password,Screenshot_Path
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.chrome.options import Options

# Create an Options object
options = Options()

# Disable the password manager and the password leak detection
options.add_experimental_option("prefs", {
    "credentials_enable_service": False,
    "profile.password_manager_enabled": False,
    "profile.password_manager_leak_detection": False  # This is the key for the "Change your password" popup
})

def test_with_valid_credentials():
    # Initialize the WebDriver with the modified options
    driver = webdriver.Chrome(options=options)
    # driver = webdriver.Chrome() # Open Chrome Browser
    try:
        driver.get(URL) # get to Open URL
        driver.find_element(By.ID,"username").send_keys(Login_Username)
        driver.find_element(By.ID,"password").send_keys(Login_Password)
        WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.CLASS_NAME,"radius"))).click()
        WebDriverWait(driver,20).until(EC.text_to_be_present_in_element((By.CLASS_NAME,"subheader"),"Welcome to the Secure Area. When you are done click logout below."))
        print("Login Successfully")
        driver.save_screenshot(Screenshot_Path+"\\"+"login.png") #Enter Your Save Screenshot Path
        driver.find_element(By.CSS_SELECTOR,"a.button.secondary.radius").click()
        print("Close button is clicked")
        time.sleep(3)
        driver.save_screenshot(Screenshot_Path+"\\"+"Logout.png")
    except Exception as e:
        print(f"Login Issue = {e}")
    finally:
        driver.quit()

if __name__ == "__main__":
    test_with_valid_credentials()