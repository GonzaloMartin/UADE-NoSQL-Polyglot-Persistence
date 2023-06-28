import sys
from controllers.LoginController import LoginHLP
from models.views import Views

sys.path.append("")
#clear = lambda: os.system('cls')

#def controllerEstadoMain(e):


view = Views()

# if __name__ == "__main__":
while True:
    usuario = view.display_login_screen()
    while usuario == None:
        usuario = view.display_login_screen()

    eleccion = view.display_main_view()
    while eleccion != 3:
        try:
            eleccion = view.display_main_view()
        except ValueError:
            print("Error, intente nuevamente")

    if eleccion == 1:
        view.display_buscar_producto_view()
    elif eleccion == 2:
        eleccion = view.display_gestionar_carrito_view()

        if eleccion == 1:
            #aca llamamos al metodo que lista el carrito
        elif eleccion == 2:
            #se debe llamar al metodo que agrega al carrito un producto, en caso de existir se deriva a modificar cantidad
        elif eleccion == 3: #modificar carrito cantidad





from controlador import CartController
from vista import CartView

# def main():
#     controller = CartController()
#     view = CartView()
#     cart_id = 'cart_id'  # Cambia esto por el identificador real del carrito
#
#     while True:
#         view.print_menu()
#         option = view.get_input("Seleccione una opción: ")
#
#         if option == '1':
#             cart = controller.list_cart(cart_id)
#             view.show_cart(cart)
#         elif option == '2':
#             product_name = view.get_input("Ingrese el nombre del producto: ")
#             product_quantity = int(view.get_input("Ingrese la cantidad del producto: "))
#             controller.add_product(cart_id, product_name, product_quantity)
#             print("Producto agregado al carrito")
#         elif option == '3':
#             product_name = view.get_input("Ingrese el nombre del producto a eliminar: ")
#             controller.remove_product(cart_id, product_name)
#             print("Producto eliminado del carrito")
#         elif option == '4':
#             product_name = view.get_input("Ingrese el nombre del producto a modificar: ")
#             new_quantity = int(view.get_input("Ingrese la nueva cantidad: "))
#             controller.modify_product(cart_id, product_name, new_quantity)
#             print("Cantidad de producto modificada en el carrito")
#         elif option == '5':
#             controller.confirm_cart(cart_id)
#             print("¡Carrito confirmado!")
#             break
#
# if __name__ == '__main__':
#     main()





