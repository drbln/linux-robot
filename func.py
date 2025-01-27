from var import *
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

def first_window():
    driver.get(link1)
    driver.find_element(By.XPATH, button1).click()

def button_click(button):
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, button))).click()

def password_field(button, passw):
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, button))).send_keys(passw)
