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




    # Métodos para gestionar la información del usuario


class Carrito:
    def __init__(self):
        self.productos = {}  # Diccionario: producto -> cantidad

    def agregar_producto(self, producto, cantidad):
        pass
        # Lógica para agregar un producto al carrito

    def eliminar_producto(self, producto):
        pass
        # Lógica para eliminar un producto del carrito

    def cambiar_cantidad(self, producto, cantidad):
        pass
        # Lógica para cambiar la cantidad de un producto en el carrito


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

