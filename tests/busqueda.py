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

time.sleep(5)

try:
    results = driver.find_elements(By.CLASS_NAME, "s-item")
    assert len(results) > 0
except AssertionError:
    driver.save_screenshot('fotos/busqueda_productos_ebay.png')
    raise

driver.quit()
