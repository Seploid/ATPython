import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

try:
    driver = webdriver.Chrome()
    url = "http://suninjuly.github.io/selects1.html"
    driver.get(url)

    num1 = int(driver.find_element(By.CSS_SELECTOR, "#num1").text)
    num2 = int(driver.find_element(By.CSS_SELECTOR, "#num2").text)

    dropdown = Select(driver.find_element(By.CSS_SELECTOR, "#dropdown"))
    dropdown.select_by_value(str(num1 + num2))

    driver.find_element(By.CSS_SELECTOR, "button").click()




finally:
    time.sleep(5)
    driver.quit()