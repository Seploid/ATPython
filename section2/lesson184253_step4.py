import math
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    #Открыть страницу http://suninjuly.github.io/alert_accept.html
    driver = webdriver.Chrome()
    driver.get("http://suninjuly.github.io/alert_accept.html")

    #Нажать на кнопку
    driver.find_element(By.CSS_SELECTOR, "button").click()

    #Принять confirm
    alert = driver.switch_to.alert
    alert.accept()

    #На новой странице решить капчу для роботов, чтобы получить число с ответом
    x = driver.find_element(By.CSS_SELECTOR, "#input_value").text
    driver.find_element(By.CSS_SELECTOR, "#answer").send_keys(calc(x))
    driver.find_element(By.CSS_SELECTOR, "button").click()



finally:
    time.sleep(5)
    driver.quit()