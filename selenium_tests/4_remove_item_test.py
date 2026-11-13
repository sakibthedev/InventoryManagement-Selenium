from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

BASE_URL = "https://your-deployed-app-url.vercel.app"

driver = webdriver.Chrome()
driver.get(f"{BASE_URL}/index.html")

try:
    # Login
    driver.find_element(By.ID, "login-email").send_keys("admin@test.com")
    driver.find_element(By.ID, "login-password").send_keys("admin123")
    driver.find_element(By.ID, "login-submit-btn").click()
    WebDriverWait(driver, 5).until(EC.url_contains("dashboard.html"))

    # Click 'Remove 1' on the first item
    remove_btn = WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable((By.CLASS_NAME, "remove-btn"))
    )
    remove_btn.click()
    time.sleep(1)

    status_text = driver.find_element(By.ID, "status-message").text
    assert "Removed 1 unit" in status_text
    print("Remove Item Quantity Test Passed!")

except Exception as e:
    print(f"Remove Item Test Failed: {e}")

finally:
    driver.quit()
