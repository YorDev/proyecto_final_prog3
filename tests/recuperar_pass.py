from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.set_window_size(1920, 1080)
driver.get("https://www.ebay.com")

sign_in_link = driver.find_element(By.LINK_TEXT, "Inicia sesión")
sign_in_link.click()

forgot_password_link = driver.find_element(By.LINK_TEXT, "¿Necesitas ayuda para iniciar sesión?")
forgot_password_link.click()

email_field = driver.find_element(By.ID, "userid")
email_field.send_keys("yordymichael05@gmail.com")

submit_button = driver.find_element(By.ID, "EMAIL_LINK_SENT")
submit_button.click()

time.sleep(5)

try:
    confirmation_message = driver.find_element(By.CLASS_NAME, "success-text")
    assert confirmation_message.is_displayed()
except AssertionError:
    driver.save_screenshot('fotos/recuperacion_contrasena_ebay.png')
    raise

driver.quit()
