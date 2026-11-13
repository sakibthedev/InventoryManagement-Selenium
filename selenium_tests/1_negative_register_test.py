from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


BASE_URL = "https://sakibthedev.github.io/InventoryManagement-Selenium"

driver = webdriver.Chrome()
driver.get(f"{BASE_URL}/register.html")

try:
   
    time.sleep(1)

    
    driver.find_element(By.ID, "reg-fullname").send_keys("Duplicate User")
    driver.find_element(By.ID, "reg-email").send_keys("admin@test.com") 
    driver.find_element(By.ID, "reg-password").send_keys("password123")
    
    time.sleep(1)
    
    
    driver.find_element(By.ID, "register-submit-btn").click()

  
    status_el = WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located((By.ID, "status-message"))
    )

 
    error_text = status_el.text.lower()
    assert "already registered" in error_text or "error" in error_text, f"Unexpected message: {status_el.text}"
    
    print("Negative Registration Test Passed! System correctly blocked the duplicate email.")
    time.sleep(2) 

except Exception as e:
    print(f"Negative Registration Test Failed: {e}")

finally:
    driver.quit()