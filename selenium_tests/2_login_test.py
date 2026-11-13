from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


BASE_URL = "https://sakibthedev.github.io/InventoryManagement-Selenium/"

driver = webdriver.Chrome()
driver.get(f"{BASE_URL}/index.html")

try:
    driver.find_element(By.ID, "login-email").send_keys("admin@test.com")
    driver.find_element(By.ID, "login-password").send_keys("admin123")
    driver.find_element(By.ID, "login-submit-btn").click()

    # Assert URL changed to dashboard.html
    expected_url = f"{BASE_URL}/dashboard.html"
    WebDriverWait(driver, 10).until(EC.url_to_be(expected_url))
    assert driver.current_url == expected_url
    print("Login Test Passed! User successfully reached dashboard.html.")

except Exception as e:
    print(f"Login Test Failed: {e}")

finally:
    driver.quit()
