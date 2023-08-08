import math
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    # Открыть страницу http://suninjuly.github.io/explicit_wait2.html
    driver = webdriver.Chrome()
    driver.get("http://suninjuly.github.io/explicit_wait2.html")

    # Дождаться, когда цена дома уменьшится до $100 (ожидание нужно установить не меньше 12 секунд)
    cart_element = driver.find_element(By.CSS_SELECTOR, ".card")
    price_element = WebDriverWait(driver, 15).until(
        expected_conditions.text_to_be_present_in_element((By.CSS_SELECTOR, ".card #price"), "$100")
    )

    # Нажать на кнопку "Book"
    cart_element.find_element(By.CSS_SELECTOR, "#book").click()

    # Решить уже известную нам математическую задачу (используйте ранее написанный код) и отправить решение
    x = driver.find_element(By.CSS_SELECTOR, "#input_value").text
    driver.find_element(By.CSS_SELECTOR, "#answer").send_keys(calc(x))
    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

finally:
    time.sleep(10)
    driver.quit()