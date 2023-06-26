from controllers.LoginController import *
from controllers.buscarProducto import *

class Views:
    def __init__(self):
        pass

    def display_login_screen(self):
        print("=== Login ===")
        username = input("Username: ")
        password = input("Password: ")
        Loginhlp = LoginHLP()
        return Loginhlp.login(username, password)

    def display_registration_screen(self):
        print("=== Registration ===")
        username = input("Username: ")
        password = input("Password: ")
        dni = input("DNI: ")
        address = input("Address: ")
        #self.controller.register(username, password, dni, address)

    def display_main_view(self):
        print("1. Buscar Producto\n"
              "2. Gestionar Carrito\n"
              "3. Cerrar Sesión\n")
        opcion= int(input("opcion: "))
        return opcion

    def display_buscar_producto_view(self):
        producto = input("Ingrese nombre del producto: ")
        productohlp = ProductoHLP()
        #result = productohlp(producto) # quizas no sea necesario devolver un result


    def display_gestionar_carrito_view(self):
        print("1. Listar carrito\n"
              "2. Agregar Producto al carrito\n"
              "3. Eliminar Producto del carrito\n"
              "4. Modificar cantidad de un producto\n"
              "5. Salir\n")
        opcion = int(input("opcion: "))
        return opcion

