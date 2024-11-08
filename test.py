# -*- coding: utf-8 -*
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.binary_location = "/opt/chromium-gost/chromium-gost"
chrome_options.add_argument("--start-maximized")

driver = webdriver.Chrome(executable_path="/home/robot/chromedriver/chromedriver-linux64/chromedriver", options=chrome_options )

driver.get("https://zakupki.gov.ru/223/ppa/public/cryptoProWarning5p.jsp?tmp=1731059967012")
driver.implicitly_wait(3)
button = driver.find_element_by_xpath("/html/body/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr[3]/td/nobr/button[2]")
ActionChains(driver) \
        .click(button) \
        .perform()


#driver.close()
