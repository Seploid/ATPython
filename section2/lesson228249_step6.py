import math
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    driver = webdriver.Chrome()
    url = "http://suninjuly.github.io/execute_script.html"

    #Открыть страницу https://SunInJuly.github.io/execute_script.html.
    driver.get(url)

    #Считать значение для переменной x.
    x = driver.find_element(By.ID, "input_value").text

    #Посчитать математическую функцию от x.
    y = calc(x)

    #Проскроллить страницу вниз.
    driver.execute_script("window.scrollBy(0, 100);")

    #Ввести ответ в текстовое поле.
    driver.find_element(By.CSS_SELECTOR, "#answer").send_keys(y)

    #Выбрать checkbox "I'm the robot".
    imRobotCheckbox = driver.find_element(By.CSS_SELECTOR, "input#robotCheckbox")
    if imRobotCheckbox.get_attribute("checked") is None:
        imRobotCheckbox.click()

    #Переключить radiobutton "Robots rule!".
    driver.find_element(By.CSS_SELECTOR, "input#robotsRule").click()

    #Нажать на кнопку "Submit".
    driver.find_element(By.CSS_SELECTOR, "button").click()

finally:
    time.sleep(5)
    driver.quit()