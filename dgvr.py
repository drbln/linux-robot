from reg import Reg, Post2
from var import driver

if __name__ == "__main__":

        automation = Reg(driver)
        automation.execute()

        posting = Post2(driver)
        posting.execute()
        driver.quit()