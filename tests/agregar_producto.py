from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()
driver.set_window_size(1920, 1080)
driver.get("https://www.ebay.com")

search_field = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.ID, "gh-ac"))
)
search_field.send_keys("laptop")
search_field.send_keys(Keys.RETURN)

product_link = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//a[contains(@class, 's-item__link')]"))
)
product_link.click()

add_to_cart_button = driver.find_element(By.ID, "isCartBtn_btn")
add_to_cart_button.click()

time.sleep(5)

try:
    cart_button = driver.find_element(By.ID, "gh-cart-i")
    assert cart_button.is_displayed()
except AssertionError:
    driver.save_screenshot('fotos/agregar_producto_carrito_ebay.png')
    raise

driver.quit()
