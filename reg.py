from func import *
from var import *
import time
import pyautogui
import threading

driver.execute_cdp_cmd('Network.clearBrowserCache', {})
driver.execute_cdp_cmd('Network.clearBrowserCookies', {})
driver.maximize_window()

thread = threading.Thread(target = first_window)
thread.start()

time.sleep(10)
pyautogui.press('enter')

button_click(button2)

button_click(button3)

button_click(button4)

password_field(button5, passw1)

button_click(button3)

button_click(button6)

time.sleep(10)
