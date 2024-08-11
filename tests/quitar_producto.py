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

remove_link = driver.find_element(By.XPATH, "//button[contains(text(), 'Remove')]")
remove_link.click()

time.sleep(5)

try:
    assert "You don't have any items in your cart" in driver.page_source
except AssertionError:
    driver.save_screenshot('fotos/eliminar_producto_carrito_ebay.png')
    raise

driver.quit()
