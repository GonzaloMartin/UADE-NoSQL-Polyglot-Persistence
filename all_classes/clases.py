class Usuario:
    def __init__(self, result):
        self.nombre = result['name']
        self.direccion = result['address']
        self.documento_identidad = result['dni']
        self.tiempoPromedio = result['tiempo_promedio']
        self.sesion = True

    def setSession(self,sesion):
        self.sesion = sesion

    def getSesion(self):
        return self.sesion



class Carrito:

    def __init__(self):
        self.ids = []
        self.nombres = []
        self.cantidad = []

    def agregar_producto(self, producto):
        if producto.id in self.ids:
            index = self.ids.index(producto.id)
            self.cantidad[index] = self.cantidad[index] + producto.cantidad
            print(f"\nEl producto {producto.nombre} ya existía en el carrito. Se ha actualizado su cantidad: {producto.cantidad}")
        else:
            self.ids.append(producto.id)
            self.nombres.append(producto.nombre)
            self.cantidad.append(producto.cantidad)

    def mostrar_carrito(self):
        if len(self.ids) == 0:
            print("El carrito está vacío.")
        else:
            print("Productos en el carrito:")
            for i in range(len(self.ids)):
                print(f"ID: {self.ids[i]}, Nombre: {self.nombres[i]}, Cantidad: {self.cantidad[i]}")




class Pedido:
    def __init__(self, carrito, cliente, detalles_precios):
        self.carrito = carrito
        self.cliente = cliente
        self.detalles_precios = detalles_precios

    # Otros métodos relacionados con la conversión del carrito en pedido


class Factura:
    def __init__(self, pedido, importe, descuentos, impuestos, detalles_pago):
        self.pedido = pedido
        self.importe = importe
        self.descuentos = descuentos
        self.impuestos = impuestos
        self.detalles_pago = detalles_pago

    # Otros métodos relacionados con la generación de facturas


class CatalogoProducto:
    def __init__(self):
        self.productos = []

    def agregar_producto(self, producto):
        pass
        # Lógica para agregar un producto al catálogo

    def actualizar_producto(self, producto):
        pass
        # Lógica para actualizar la información de un producto en el catálogo

    def eliminar_producto(self, producto):
        pass
        # Lógica para eliminar un producto del catálogo


class RegistroCambiosCatalogo:
    def __init__(self, producto, valor_anterior, nuevo_valor, operador):
        self.producto = producto
        self.valor_anterior = valor_anterior
        self.nuevo_valor = nuevo_valor
        self.operador = operador


class Sesion:
    def __init__(self, nombre, direccion, documento_identidad):
        self.nombre = nombre
        self.direccion = direccion
        self.documento_identidad = documento_identidad

    # Métodos para gestionar la sesión del usuario


class ActividadUsuario:
    def __init__(self, sesion, duracion):
        self.sesion = sesion
        self.duracion = duracion

    # Lógica para determinar la categorización del usuario (TOP, MEDIUM, LOW)


class OperacionFacturacion:
    def __init__(self, medio_pago, operador, fecha, hora, monto):
        self.medio_pago = medio_pago
        self.operador = operador
        self.fecha = fecha
        self.hora = hora
        self.monto = monto


class Pago:
    def __init__(self, forma_pago, operador, fecha, hora, monto):
        self.forma_pago = forma_pago
        self.operador = operador
        self.fecha = fecha
        self.hora = hora
        self.monto = monto

    # Otros métodos relacionados con la gestión de pagos

class Producto:
    def __init__(self, id, nombre, precio, cantidad, categoria, descripcion):
        self.id = id
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad
        self.categoria = categoria
        self.descripcion= descripcion

    def __str__(self):
        return f"\nNombre: {self.nombre}\nPrecio: {self.precio}\nCategoría: {self.categoria}\nDescripción: {self.descripcion}"
