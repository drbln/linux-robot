from reg import Reg
from reg import Post
from var import driver

if __name__ == "__main__":
    automation = Reg(driver)
    automation.execute()

    posting = Post(driver)
    posting.perform_actions()
