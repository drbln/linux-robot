from func import *
from var import *
import time
import pyautogui
import threading



class Reg:
    def __init__(self, driver):
        self.driver = driver

    def clear_browser_data(self):
        """Очистка кеша и куки браузера."""
        self.driver.execute_cdp_cmd('Network.clearBrowserCache', {})
        self.driver.execute_cdp_cmd('Network.clearBrowserCookies', {})
        self.driver.maximize_window()

    def run_first_window(self):
        """Запуск первого окна в отдельном потоке."""
        thread = threading.Thread(target=first_window)
        thread.start()
        time.sleep(20)
        pyautogui.press('enter')

    def perform_actions(self):
        """Выполнение основной последовательности действий."""
        button_click(button2)
        button_click(button3)
        button_click(button4)
        password_field(button5, passw1)
        button_click(button3)
        button_click(button6)
        time.sleep(10)

    def execute(self):
        """Основной метод для выполнения действий с обработкой ошибок."""
        while True:
            try:
                self.clear_browser_data()
                self.run_first_window()
                self.perform_actions()
                break
            except Exception as e:
                self.driver.refresh()
                time.sleep(5)


class Post:
    def __init__(self, driver):
        self.driver = driver
    
    def perform_actions(self):
        #Выполнение основной последовательности действий
        button_click(button10)
        skip_warnings()
        button_click(button11)
        time.sleep(10)
        switch_New_window()
        button_click(button12)
        button_click(button13)
        switch_New_window()
        time.sleep(10)

    def execute(self):
        follow_the_link(link2)
        while True:
            if button_check(driver, button7):
                try:
                    button_click(button7)
                    self.perform_actions()

                except:
                    self.driver.quit()
                    time.sleep(5)
            else: 
                break

  
