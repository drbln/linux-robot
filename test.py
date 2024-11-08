from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.binary_location = "/opt/chromium-gost/chromium-gost"

driver = webdriver.Chrome(executable_path="/home/robot/chromedriver/chromedriver-linux64/chromedriver", options=chrome_options )

driver.get("https://python.org")

print(driver.title)



#driver.close()
