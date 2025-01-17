from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service

# Укажите путь к драйверу и браузеру Chromium-GOST
chromium_path = "/opt/chromium-gost/chromium-gost"
webdriver_path = "/home/robot/chromedriver/chromedriver-linux64/chromedriver"

# Настройка опций для Chromium-GOST
options = webdriver.ChromeOptions()
options.binary_location = chromium_path  # Указываем путь к Chromium-GOST

# Инициализация веб-драйвера
service = Service(webdriver_path)  # Указываем путь к веб-драйверу
driver = webdriver.Chrome(service=service, options=options)

try:
    # Открыть целевую страницу
    driver.get("https://zakupki.gov.ru/223/ppa/public/cryptoProWarning5p.jsp?tmp=1737012796746")

    # Ожидание кнопки и нажатие
    button = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Продолжить работу')]"))
    )
    button.click()

    # Дальнейшая работа на сайте
    print("Кнопка успешно нажата.")
except Exception as e:
    print(f"Произошла ошибка: {e}")
