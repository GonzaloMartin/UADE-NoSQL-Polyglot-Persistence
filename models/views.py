from controllers.LoginController import *
from controllers.buscarProducto import BuscarProducto
from controllers.confirmar_carrito import ConfirmarCarrito

class Views:
    def __init__(self):
        self.buscar_producto = BuscarProducto()
        self.confirmar_carrito = ConfirmarCarrito()

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
              "3. Eliminar Producto del carrito\n"
              "4. Modificar cantidad de un producto\n"
              "5. Salir\n")
        opcion = int(input("opcion: "))
        return opcion

    def display_confirmar_carrito_view(self, carrito, cliente):
        print("-- Confirmación de Carrito --")
        print("ID Producto - Descripción - Cantidad - Precio Unitario")  # header
        for item in carrito:
            print(f"{item['id']} - {item['descripcion']} - {item['cantidad']} - {item['precio_unitario']}")

        impuestos = self.confirmar_carrito.calcular_impuestos(carrito)
        print(f"Impuestos IVA 21%: {impuestos}")

        tipo_descuento, descuento_porcentaje, importe_descuento = self.confirmar_carrito.calcular_descuento(cliente)
        print(f"Descuentos: {tipo_descuento} ({descuento_porcentaje}%) -{importe_descuento}")

        importe_total = self.confirmar_carrito.calcular_importe_total(carrito, impuestos, importe_descuento)
        print(f"Importe TOTAL: {importe_total}")

        print("\nDatos del cliente:")
        print(f"Nombre y Apellido: {cliente['nombre']} {cliente['apellido']}")
        print(f"Dirección: {cliente['direccion']}")
        print(f"DNI: {cliente['dni']}")

        print("\n1. Confirmar")
        print("2. Volver")

        opcion = int(input("Seleccionar: "))
        if opcion == 1:
            self.procesar_confirmacion_carrito(carrito)
        elif opcion == 2:
            return
        else:
            print("Opción inválida.")

    def procesar_confirmacion_carrito(self, carrito):
        print("Elija un Tipo de pago para Finalizar la compra:\n"
              "1. Efectivo.\n"
              "2. Tarjeta de Crédito.\n"
              "3. Cuenta Corriente.\n"
              "0. Volver.\n")
        opcion = input("Seleccionar tipo de pago: ")
        if opcion == 1 or opcion == 2 or opcion == 3:
            print("Compra confirmada.")
            self.confirmar_carrito.insertar_datos_cassandra(carrito)
        elif opcion == 0:
            return
        else:
            print("Opción inválida.")
