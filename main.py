from reg import Reg, Post
from var import driver
import time

if __name__ == "__main__":
    while True:
        automation = Reg(driver)
        automation.execute()

        posting = Post(driver)
        posting.execute()

        driver.quit()
        time.sleep(900)

