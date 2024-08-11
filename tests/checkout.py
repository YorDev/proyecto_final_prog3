from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.set_window_size(1920, 1080)
driver.get("https://www.ebay.com")

search_field = driver.find_element(By.ID, "gh-ac")
search_field.send_keys("laptop")
search_field.send_keys(Keys.RETURN)

product_link = driver.find_element(By.XPATH, "//a[contains(@class, 's-item__link')]")
product_link.click()

add_to_cart_button = driver.find_element(By.ID, "isCartBtn_btn")
add_to_cart_button.click()

time.sleep(5)

cart_button = driver.find_element(By.ID, "gh-cart-i")
cart_button.click()

checkout_button = driver.find_element(By.ID, "ptcBtnRight")
checkout_button.click()

time.sleep(5)

try:
    assert "Secure Checkout" in driver.page_source
except AssertionError:
    driver.save_screenshot('fotos/proceso_checkout_ebay.png')
    raise

driver.quit()
