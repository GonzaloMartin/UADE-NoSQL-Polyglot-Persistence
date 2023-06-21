from LoginController import *

class LoginView:
    def __init__(self, controller):
        self.controller = controller

    def display_login_screen(self):
        print("=== Login ===")
        username = input("Username: ")
        password = input("Password: ")
        self.controller.login(username, password)

    def display_registration_screen(self):
        print("=== Registration ===")
        username = input("Username: ")
        password = input("Password: ")
        dni = input("DNI: ")
        address = input("Address: ")
        self.controller.register(username, password, dni, address)
