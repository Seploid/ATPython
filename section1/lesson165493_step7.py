import math
import time

from selenium import webdriver
from selenium.webdriver.common.by import By


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    driver = webdriver.Chrome()
    url = "http://suninjuly.github.io/get_attribute.html"
    driver.get(url)

    box = driver.find_element(By.CSS_SELECTOR, "[valuex]")

    x = box.get_attribute("valuex")
    y = calc(x)
    driver.find_element(By.CSS_SELECTOR, "#answer").send_keys(y)

    imRobotCheckbox = driver.find_element(By.CSS_SELECTOR, "input#robotCheckbox")

    if imRobotCheckbox.get_attribute("checked") is None:
        imRobotCheckbox.click()

    driver.find_element(By.CSS_SELECTOR, "input#robotsRule").click()
    driver.find_element(By.CSS_SELECTOR, "button").click()

finally:
    time.sleep(10)
    driver.quit()