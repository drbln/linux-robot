from selenium import webdriver
from selenium.webdriver.chrome.service import Service

# Укажите путь к драйверу и браузеру Chromium-GOST
chromium_path = "/opt/chromium-gost/chromium-gost"
webdriver_path = "/home/robot/chromedriver-linux64/chromedriver"

# Настройка опций для Chromium-GOST
options = webdriver.ChromeOptions()

# Указываем путь к Chromium-GOST
options.binary_location = chromium_path 

# Инициализация веб-драйвера
service = Service(webdriver_path)  # Указываем путь к веб-драйверу
driver = webdriver.Chrome(service=service, options=options)

passw1 = "12345"

# Используеммый ссылки:
# Ccылка Авторизации
link1 = "https://zakupki.gov.ru/223/ppa/public/cryptoProWarning5p.html"
# Ccылка для извещений
link2 = "https://lk.zakupki.gov.ru/223/purchase/private/notification/search.html?customerOrgId=&creatorAgencyId=&purchaseMethodId=&purchaseNumber=&purchaseName=&creatorAgency=&_createdCustomerRepresentative=on&_createdBlockedCustomer=on&purchaseMethodName=&purchaseStages=NOTICE_FORMATION&_purchaseStages=on&_purchaseStages=on&purchaseStages=APPLICATION_FILING&_purchaseStages=on&_purchaseStages=on&purchaseStages=COMMISSION_ACTIVITIES&_purchaseStages=on&purchaseDescription=&organName=&okpd2Id=&okpd2Text=&okpd2Code=&organName=&okved2Id=&okved2Text=&okved2Code=&_needAuthorizedConfirmationOnly=on&_fromElectronicMarketplace=on&_importedFromVSRI=on&_importedFromKISRMIS=on&_unpublishedDataExists=on&_cooperativeOnly=on&_onlyNotPlacement=on&activeTab=0&pageCounts=0,0,0,0,0,0"
# Ccылка договоров


# Блок кнопок для использования
## При авторизации
button1 = "//button[contains(text(), 'Продолжить работу')]"
button2 = "//button[contains(text(), 'Эл. подпись')]"
button3 = "//button[contains(text(), 'Продолжить')]"
button4 = "/html/body/esia-root/div/esia-login/div/div/esia-eds/div/button[1]/h3" # Стрелка при выборе ЭЦП
button5 = "/html/body/esia-root/esia-modal/div/div[2]/div/ng-component/div/article/div[4]/div[2]/div[1]/esia-input-password/div/input" # Поле для заполнения пароля
button6 = "//button[contains(text(), 'Подтвердить')]"
## Для размещения
### Первые 3 обьекта
button7 = "/html/body/div[3]/div[2]/div[1]/div[3]/div[2]/div/form/div[2]/div[2]/table/tbody/tr[1]/td[2]/div[2]/img"
button8 = "/html/body/div[3]/div[2]/div[1]/div[3]/div[2]/div/form/div[2]/div[2]/table/tbody/tr[2]/td[2]/div[2]/img"
button9 = "/html/body/div[3]/div[2]/div[1]/div[3]/div[2]/div/form/div[2]/div[2]/table/tbody/tr[3]/td[2]/div[2]/img"
#### Стрелка и кнопка разместить
button10 = "/html/body/div[3]/div[2]/div[1]/div[3]/div[2]/div/form/div[2]/div[2]/table/tbody/tr[1]/td[2]/div[2]/div/ul/li[1]/a" 
button11 = "/html/body/div[5]/div/form/div[3]/button[1]"

## При размещении
button12 = "/html/body/div[3]/div[4]/a[2]/input"
button13 = "/html/body/div[5]/div/form/div[4]/button[2]"
