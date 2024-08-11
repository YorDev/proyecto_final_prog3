from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.set_window_size(1920, 1080)
driver.get("https://www.ebay.com")

sign_in_link = driver.find_element(By.LINK_TEXT, "Sign in")
sign_in_link.click()

email_field = driver.find_element(By.ID, "userid")
email_field.send_keys("prueba73483502934092842")

sign_in_button = driver.find_element(By.ID, "signin-continue-btn")
sign_in_button.click()

time.sleep(5)

try:
    error_message = driver.find_element(By.ID, "errf")
    assert error_message.is_displayed()
except AssertionError:
    driver.save_screenshot('fotos/inicio_sesion_fallido_ebay.png')
    raise

driver.quit()
