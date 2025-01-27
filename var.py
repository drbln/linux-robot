from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By

# Укажите путь к драйверу и браузеру Chromium-GOST
chromium_path = "/opt/chromium-gost/chromium-gost"
webdriver_path = "/home/robot/chromedriver/chromedriver-linux64/chromedriver"

# Настройка опций для Chromium-GOST
options = webdriver.ChromeOptions()

# Указываем путь к Chromium-GOST
options.binary_location = chromium_path 

# Инициализация веб-драйвера
service = Service(webdriver_path)  # Указываем путь к веб-драйверу
driver = webdriver.Chrome(service=service, options=options)

passw1 = "12345"

link1 = "https://zakupki.gov.ru/223/ppa/public/cryptoProWarning5p.html"

button1 = "//button[contains(text(), 'Продолжить работу')]"

button2 = "//button[contains(text(), 'Эл. подпись')]"

button3 = "//button[contains(text(), 'Продолжить')]"

# Стрелка при выборе ЭЦП
button4 = "/html/body/esia-root/div/esia-login/div/div/esia-eds/div/button[1]/h3"

# Поле для заполнения пароля
button5 = "/html/body/esia-root/esia-modal/div/div[2]/div/ng-component/div/article/div[4]/div[2]/div[1]/esia-input-password/div/input"

button6 = "//button[contains(text(), 'Подтвердить')]"
