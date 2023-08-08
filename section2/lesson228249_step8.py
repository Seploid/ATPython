import math
import os
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

def path_of_file(file_name):
    print(os.path.abspath(__file__))
    print(os.path.abspath(os.path.dirname(__file__)))
    return os.path.join(os.path.dirname(__file__), file_name)

try:
    driver = webdriver.Chrome()
    url = "http://suninjuly.github.io/file_input.html"

    #Открыть страницу https://SunInJuly.github.io/execute_script.html.
    driver.get(url)

    #Заполнить текстовые поля: имя, фамилия, email
    driver.find_element(By.NAME, "firstname").send_keys("Юрий")
    driver.find_element(By.NAME, "lastname").send_keys("Разживин")
    driver.find_element(By.NAME, "email").send_keys("dsfsdfds@sdff.df")

    #Загрузить файл. Файл должен иметь расширение .txt и может быть пустым
    driver.find_element(By.NAME, "file").send_keys(path_of_file("download.txt"))

    #Нажать на кнопку "Submit".
    driver.find_element(By.CSS_SELECTOR, "button").click()

finally:
    time.sleep(5)
    driver.quit()