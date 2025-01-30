from var import *
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait


def first_window():
    driver.get(link1)
    driver.find_element(By.XPATH, button1).click()

def button_click(button):
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, button))).click()

def password_field(button, passw):
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, button))).send_keys(passw)

def follow_the_link(link):
    driver.get(link)

def switch_New_window():
    main_window_handle = driver.current_window_handle
    all_window_handles = driver.window_handles
    for handle in all_window_handles:
        if handle != main_window_handle:
            driver.switch_to.window(handle)
            break

def skip_warnings():
    while True:
            try:
                WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#dialogDiv > div:nth-child(3) > a:nth-child(1) > input"))).click()
            except Exception as e:
                print(f"Произошла ошибка: {e}")
                break

