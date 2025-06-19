# linux-robot

## Подготовка машины для работы с ЭЦП

Настройка плагина госуслуг

wget https://www.cryptopro.ru/sites/default/files/public/faq/ifcx64.cfg

sudo cp ~/ifcx64.cfg /etc/ifc.cfg

/opt/cprocsp/bin/amd64/csptestf -absorb -certs -autoprov

sudo cp /etc/opt/chrome/native-messaging-hosts/ru.rtlabs.ifcplugin.json /etc/chromium/native-messaging-hosts

## Подготовка машины для работы с Selenium

Для добавления движка хромиум скачиваем версию соответствующую chromium-gost

wget https://storage.googleapis.com/chrome-for-testing-public/137.0.7151.69/linux64/chromedriver-linux64.zip

chmod +x /home/robot/chromedriver-linux64/chromedriver

Путь до движка в переменной webdriver_path

Скачиваем webdiver нужной версии https://googlechromelabs.github.io/chrome-for-testing/

sudo apt install python3 python3-pip -y

pip3 install selenium pyautogui

sudo apt install python3-tk python3-dev
