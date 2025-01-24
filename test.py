from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
import keyboard
import time
import pyautogui
import threading
import os
import shutil

# Укажите путь к драйверу и браузеру Chromium-GOST
chromium_path = "/opt/chromium-gost/chromium-gost"
webdriver_path = "/home/robot/chromedriver/chromedriver-linux64/chromedriver"

# Настройка опций для Chromium-GOST
options = webdriver.ChromeOptions()
options.binary_location = chromium_path  # Указываем путь к Chromium-GOST


# Инициализация веб-драйвера
service = Service(webdriver_path)  # Указываем путь к веб-драйверу
driver = webdriver.Chrome(service=service, options=options)
driver.maximize_window()


driver.execute_cdp_cmd('Network.clearBrowserCache', {})
driver.execute_cdp_cmd('Network.clearBrowserCookies', {})

    

# Запускаем нажаните кнопки в отдельном потоке
def perform_action():
    driver.get("https://zakupki.gov.ru/223/ppa/public/cryptoProWarning5p.html")
    button = driver.find_element(By.XPATH, "//button[contains(text(), 'Продолжить работу')]")
    button.click()

thread = threading.Thread(target=perform_action)
thread.start()

# Ждем 3 секунды и нажимает Enter
time.sleep(10)
pyautogui.press('enter')

button = WebDriverWait(driver, 20).until(
    EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Эл. подпись')]"))
)
button.click()

button = WebDriverWait(driver, 20).until(
    EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Продолжить')]"))
)
button.click()

button = WebDriverWait(driver, 20).until(
    EC.element_to_be_clickable((By.XPATH, "/html/body/esia-root/div/esia-login/div/div/esia-eds/div/button[1]/h3"))
)
button.click()

password_field = WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.XPATH, "/html/body/esia-root/esia-modal/div/div[2]/div/ng-component/div/article/div[4]/div[2]/div[1]/esia-input-password/div/input"))
)
password_field.send_keys("12345")

button = WebDriverWait(driver, 20).until(
    EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Продолжить')]"))
)
button.click()

button = WebDriverWait(driver, 20).until(
    EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Подтвердить')]"))
)
button.click()

time.sleep(20)
