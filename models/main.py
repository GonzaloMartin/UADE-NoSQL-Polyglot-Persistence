import sys
from LoginController import LoginHLP
#from controllers.mongo_hlp import *
from login import LoginView
sys.path.append("../..")

if __name__ == "__main__":
    controller = LoginHLP()
    view = LoginView(controller)
    view.display_login_screen()
