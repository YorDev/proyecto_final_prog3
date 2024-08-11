from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.set_window_size(1920, 1080)
driver.get("https://www.ebay.com")

sign_in_link = driver.find_element(By.LINK_TEXT, "Inicia sesión")
sign_in_link.click()

email_field = driver.find_element(By.ID, "userid")
email_field.send_keys("YordyMagallanes@gmail.com")

password_field = driver.find_element(By.ID, "pass")
password_field.send_keys("contraseñadeprueba@20220538")

sign_in_button = driver.find_element(By.ID, "sgnBt")
sign_in_button.click()

time.sleep(5) 

try:
    user_icon = driver.find_element(By.ID, "gh-ug")
    assert user_icon.is_displayed()
except AssertionError:
    driver.save_screenshot('fotos/inicio_sesion_funcional_ebay.png')
    raise

driver.quit()
