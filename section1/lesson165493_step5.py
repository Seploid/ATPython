import math
import time

from selenium import webdriver
from selenium.webdriver.common.by import By


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    driver = webdriver.Chrome()
    link = "https://suninjuly.github.io/math.html"
    driver.get(link)

    x = driver.find_element(By.CSS_SELECTOR, "#input_value").text
    y = calc(x)
    driver.find_element(By.CSS_SELECTOR, "#answer").send_keys(y)

    imRobotCheckbox = driver.find_element(By.CSS_SELECTOR, "label[for='robotCheckbox']")

    if imRobotCheckbox.get_attribute("checked") is None:
        imRobotCheckbox.click()

    driver.find_element(By.CSS_SELECTOR, "label[for='robotsRule']").click()
    driver.find_element(By.CSS_SELECTOR, "button").click()


finally:
    time.sleep(10)
    driver.quit()

