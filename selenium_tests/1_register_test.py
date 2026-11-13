from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

BASE_URL = "https://sakibthedev.github.io/InventoryManagement-Selenium/"

driver = webdriver.Chrome()

driver.get(f"{BASE_URL}/register.html")

try:
    driver.find_element(By.ID, "reg-fullname").send_keys("Test Student")
    driver.find_element(By.ID, "reg-email").send_keys("student@test.com")
    driver.find_element(By.ID, "reg-password").send_keys("pass1234")
    driver.find_element(By.ID, "register-submit-btn").click()

    # Wait for redirect back to index.html (Login page)
    WebDriverWait(driver, 5).until(EC.url_contains("index.html"))
    assert "index.html" in driver.current_url
    print("Registration Test Passed! Redirected to login page.")

except Exception as e:
    print(f"Registration Test Failed: {e}")

finally:
    driver.quit()
