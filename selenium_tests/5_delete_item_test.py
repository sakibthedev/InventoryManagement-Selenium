from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

BASE_URL = "https://sakibthedev.github.io/InventoryManagement-Selenium/"

driver = webdriver.Chrome()
driver.get(f"{BASE_URL}/index.html")

try:
    
    driver.find_element(By.ID, "login-email").send_keys("admin@test.com")
    driver.find_element(By.ID, "login-password").send_keys("admin123")
    driver.find_element(By.ID, "login-submit-btn").click()
    WebDriverWait(driver, 5).until(EC.url_contains("dashboard.html"))

  
    driver.find_element(By.ID, "item-name").send_keys("Temp Item To Delete")
    driver.find_element(By.ID, "item-category").send_keys("Misc")
    driver.find_element(By.ID, "item-quantity").send_keys("2")
    driver.find_element(By.ID, "add-item-btn").click()
    time.sleep(1)

   
    delete_buttons = driver.find_elements(By.CLASS_NAME, "delete-btn")
    delete_buttons[-1].click()
    time.sleep(1)

    assert "Temp Item To Delete" not in driver.page_source
    print("Delete Item Test Passed!")

except Exception as e:
    print(f"Delete Item Test Failed: {e}")

finally:
    driver.quit()
