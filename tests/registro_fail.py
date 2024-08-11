from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.set_window_size(1920, 1080)
driver.get("https://www.ebay.com")

register_link = driver.find_element(By.LINK_TEXT, "regístrate")
register_link.click()

first_name_field = driver.find_element(By.ID, "firstname")
first_name_field.send_keys("Yordy")

last_name_field = driver.find_element(By.ID, "lastname")
last_name_field.send_keys("Magallanes")

email_field = driver.find_element(By.ID, "Email")
email_field.send_keys("yordymichael05@gmail.com")

password_field = driver.find_element(By.ID, "password")
password_field.send_keys("contraseñadeprueba@20220538")

register_button = driver.find_element(By.ID, "EMAIL_REG_FORM_SUBMIT")
register_button.click()

time.sleep(5)

try:
    welcome_message = driver.find_element(By.XPATH, "//h1[contains(text(), 'Welcome')]")
    assert welcome_message.is_displayed()
except AssertionError:
    driver.save_screenshot('fotos/registro_fallido_ebay.png')
    raise

driver.quit()
