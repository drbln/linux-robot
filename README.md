# linux-robot

Для добавления движка хромиум скачиваем его  wget https://storage.googleapis.com/chrome-for-testing-public/130.0.6723.116/linux64/chromedriver-linux64.zip

Разархивируем что бы конечный путь был /home/robot/chromedriver/chromedriver-linux64

Скачиваем webdiver нужной версии https://googlechromelabs.github.io/chrome-for-testing/


Настройка плагина госуслуг

wget https://www.cryptopro.ru/sites/default/files/public/faq/ifcx64.cfg
sudo cp ~/ifcx64.cfg /etc/ifc.cfg

/opt/cprocsp/bin/amd64/csptestf -absorb -certs -autoprov

sudo cp /etc/opt/chrome/native-messaging-hosts/ru.rtlabs.ifcplugin.json /etc/chromium/native-messaging-hosts
