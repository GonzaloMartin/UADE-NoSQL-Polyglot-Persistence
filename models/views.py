from controllers.LoginController import *
from controllers.buscarProducto import BuscarProducto

class Views:
    def __init__(self):
        self.buscar_producto = BuscarProducto()

    def display_login_screen(self):
        print("=== Login ===")
        username = input("Username: ")
        password = input("Password: ")
        login_hlp = LoginHLP()
        return login_hlp.login(username, password)

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
        opcion = int(input("opcion: "))
        return opcion

    def display_buscar_producto_view(self):
        print("-- Buscar producto --")
        producto = input("Ingrese el producto que desea buscar: ")
        collection = 'productos'
        resultados = self.buscar_producto.buscar_producto(producto, collection)

        if len(resultados) > 0:
            print("Resultados de búsqueda:")
            for i, prod in enumerate(resultados):
                print(f"{i + 1}. {prod['nombre']} ${prod['precio']}")
                print("-----------------------")

            seleccion = input("Seleccione el número de producto para ver los detalles: ")
            if seleccion.isdigit() and int(seleccion) in range(1, len(resultados) + 1):
                producto_seleccionado = resultados[int(seleccion) - 1]
                self.display_detalle_producto_view(producto_seleccionado)
            else:
                print("Selección inválida.")
        else:
            print("No se encontraron resultados.")

    def display_detalle_producto_view(self, producto):
        print()
        print("-- Detalle del producto --")
        print(f"* ID: {producto['id']}")
        print(f"* Nombre: {producto['nombre']}")
        print(f"* Precio: ${producto['precio']}")
        print(f"* Categoría: {producto['categoria']}")
        print(f"* Descripción: {producto['descripción']}")
        print("1. Agregar al carrito")
        print("2. Volver al menú principal")
        seleccion = int(input("Seleccionar: "))
        if seleccion == 1:
            print()
            print("-- Carrito de compras --")
            cantidad = int(input("Indicar cantidad: "))
            print("1. Aceptar e ir al carrito")
            print("2. Volver al menú principal")
            seleccion = int(input("Seleccionar: "))
            if seleccion == 1:
                print(f"Cantidad seleccionada: {cantidad}")
                print()

            elif seleccion == 2:
                return
            else:
                print("Opción inválida.")
        elif seleccion == 2:
            return
        else:
            print("Opción inválida.")

    def display_gestionar_carrito_view(self):
        print("1. Listar carrito\n"
              "2. Agregar Producto al carrito\n"
              "3. Modificar cantidad de un producto\n"
              "4. Eliminar Producto del carrito\n"
              "5. Confirmar carrito\n"
              "6. Salir\n")

        opcion = int(input("opcion: "))
        return opcion




