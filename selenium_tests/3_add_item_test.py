from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

BASE_URL = "https://your-deployed-app-url.vercel.app"

driver = webdriver.Chrome()
driver.get(f"{BASE_URL}/index.html")

try:
    # Login
    driver.find_element(By.ID, "login-email").send_keys("admin@test.com")
    driver.find_element(By.ID, "login-password").send_keys("admin123")
    driver.find_element(By.ID, "login-submit-btn").click()
    WebDriverWait(driver, 5).until(EC.url_contains("dashboard.html"))

    # Add Item
    driver.find_element(By.ID, "item-name").send_keys("Wireless Mouse")
    driver.find_element(By.ID, "item-category").send_keys("Electronics")
    driver.find_element(By.ID, "item-quantity").send_keys("10")
    driver.find_element(By.ID, "add-item-btn").click()

    WebDriverWait(driver, 5).until(lambda d: "Wireless Mouse" in d.page_source)
    print("Add Item Test Passed!")

except Exception as e:
    print(f"Add Item Test Failed: {e}")

finally:
    driver.quit()
