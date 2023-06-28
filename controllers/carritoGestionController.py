import sys
from controllers.mongo_hlp import *
from all_classes.clases import cart_manager
sys.path.append("../../..")


class CartController:
    def __init__(self):
        self.cart_manager = cart_manager()

    def list_cart(self, cart_id):
        cart = self.cart_manager.get_cart()
        return cart

    def add_product(self, cart_id, product_name, product_quantity):
        cart = self.cart_manager.get_cart()
        new_product = {'name': product_name, 'quantity': product_quantity}
        cart['products'].append(new_product)
        self.cart_manager.update_cart(cart_id, cart)

    def remove_product(self, cart_id, product_name):
        cart = self.cart_manager.get_cart(cart_id)
        cart['products'] = [product for product in cart['products'] if product['name'] != product_name]
        self.cart_manager.update_cart(cart_id, cart)

    def modify_product(self, cart_id, product_name, new_quantity):
        cart = self.cart_manager.get_cart(cart_id)
        for product in cart['products']:
            if product['name'] == product_name:
                product['quantity'] = new_quantity
                break
        self.cart_manager.update_cart(cart_id, cart)

    def confirm_cart(self, cart_id):
        cart = self.cart_manager.get_cart(cart_id)
        # Realizar las acciones necesarias al confirmar el carrito
        # se podria hacer con un IF?

        while True:
            print("----- Opciones del Carrito -----")
            print("1. Confirmar carrito")
            print("2. Volver a la pantalla inicial")

           option = input("Seleccione una opción: ")

            if option == '1':
                self.select_payment(cart)
                break
            elif option == '2':
                break
            else:
                print("Opción inválida. Por favor, seleccione una opción válida.")
