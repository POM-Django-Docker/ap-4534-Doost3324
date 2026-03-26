from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
wait = WebDriverWait(driver, 30)

driver.get("http://127.0.0.1:8000/")

login_btn = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Login")))
login_btn.click()

wait.until(EC.presence_of_element_located((By.NAME, "email"))).send_keys("saputsdhgdhjiyr@gmail.com")
driver.find_element(By.NAME, "password").send_keys("1111")

driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

logout_btn = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Logout']")))

print("Login successful")

logout_btn.click()

wait.until(EC.presence_of_element_located((By.LINK_TEXT, "Login")))
print("Logout successful")

driver.find_element(By.LINK_TEXT, "Login").click()

wait.until(EC.presence_of_element_located((By.NAME, "email"))).send_keys("doofus@gmail.com")
driver.find_element(By.NAME, "password").send_keys("doofusisabum")

driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

error = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "text-danger")))
print("Error:", error.text)

driver.quit()