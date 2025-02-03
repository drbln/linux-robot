from reg import Reg, Post
from var import driver

if __name__ == "__main__":

        automation = Reg(driver)
        automation.execute()

        posting = Post(driver)
        posting.execute()
        driver.quit()
