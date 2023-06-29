from controllers.LoginController import *
from controllers.catalogo_productos_controller import catalogo_productos
from controllers.carrito_controller import carrito_controller
from controllers.confirmar_carrito import ConfirmarCarrito

class Views:

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
        print("\n1. Buscar Producto"
              "\n2. Gestionar Carrito"
              "\n3. Cerrar Sesión")
        try:
            opcion = int(input("opcion: "))
        except ValueError:
            return
        return opcion

    def display_catalogo_productos_view(self):
        print("-- Buscar producto --")
        producto = input("Ingrese el producto que desea buscar: ")
        catalogo = catalogo_productos()
        resultados = catalogo.buscar(producto) #resultados tiene la lista de productos
        if resultados != None:
            catalogo.mostrar_catalogo(resultados) #se muestran los resultados
            try:
                seleccion = int(input("Seleccione el número de producto para ver los detalles: "))
                producto_seleccionado = catalogo.seleccionar_producto(seleccion,catalogo.buscar(producto)) #devuelve el producto (obj) si no existe, None
                if producto_seleccionado != None:
                    print(producto_seleccionado)
                    print("\n1. Agregar al carrito")
                    print("2. Volver al menú principal")
                    seleccion = int(input("Seleccionar: "))
                    if seleccion == 1:
                        cantidad = int(input("\nSeleccione la cantidad: "))
                        producto_seleccionado.cantidad = cantidad
                        carrito = carrito_controller()
                        carrito.agregarProducto(producto_seleccionado)  # se agrega el producto
                        return carrito
                    elif seleccion == 2:
                        return
                    else:
                        print("Opción inválida.")
                else:
                    print("Selección inválida")
            except ValueError:
                print("Selección no válida")
        else:
            print("No se encontraron resultados.")


    def display_gestionar_carrito_view(self,carrito):
        print("\n1. Listar carrito"
              "\n2. Agregar Producto al carrito"
              "\n3. Eliminar Producto del carrito"
              "\n4. Modificar cantidad de un producto"
              "\n5. Salir")
        opcion = int(input("opcion: "))
        if opcion == 1:
            carrito.mostrarCarrito()



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
