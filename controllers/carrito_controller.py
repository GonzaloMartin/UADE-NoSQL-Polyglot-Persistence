from controllers.mongo_hlp import MongoHelper
from controllers.cassandra_hlp import CassandraHelper
from all_classes.clases import Producto

class carrito_controller:
    def __init__(self):
        self.mongo_helper = MongoHelper()
        self.mongo_helper.conectar()
        self.mongo_helper.usar_db('bdd2')
        self.collection = "carrito"
        self.cassandra_helper = CassandraHelper()
        # hace falta agregar un atributo "estado" para el carrito

    def existeCarrito(self):
        return self.mongo_helper.exists_documents(self.collection)

    def existeProductoEnCarrito(self,prod):
        return self.mongo_helper.get_document_by_id(self.collection,prod.id)

    def getDocProducto(self,id):
        return self.mongo_helper.get_document_by_id(self.collection,id)

    def getProductofromDoc(self,id): # este controlador debería estar en productos controller
        documento = self.getDocProducto(id)
        producto = Producto(documento['id'], documento['nombre'], documento['precio'], 0, documento['categoria'],
        documento['descripcion'])
        return producto

    def agregarProducto(self,producto):
        try: # se agrega el producto al carrito
            if self.existeCarrito() is None or (self.existeCarrito() and self.existeProductoEnCarrito(producto) is None):
                # se agrega el producto
                query = {
                    'id': producto.id,
                    'nombre': producto.nombre,
                    'precio': producto.precio,
                    'cantidad': producto.cantidad,
                    'categoria': producto.categoria,
                    'descripcion': producto.descripcion
                }
                self.mongo_helper.insert_document('carrito',query)
                print("Agregado al carrito!")
            else: # se actualiza la cantidad del producto
                try:
                    print("ATENCION: El producto existe y se fijará una nueva Cantidad.")
                    print("Continuar? (s/n)")
                    optCantidad = input()
                    if optCantidad == 's':
                        # Realizar la actualización
                        # doc = self.mongo_helper.get_document_by_id(self.collection,producto.id)
                        # cantidadActual = doc['cantidad']
                        query = (
                            {'$set': {'cantidad':producto.cantidad}}
                        )
                        self.mongo_helper.update_document(self.collection,producto.id,query)
                        print('Actualización Exitosa.')
                    else:
                        pass
                except Exception as e:
                    print('Error al actualizar la cantidad:', e)
        except Exception as e:
            print("se ha producido un error a la hora de cargar el producto al carrito:", e)

    def eliminar_producto_por_posicion(self, posicion):
        carrito = self.mongo_helper.get_collection(self.collection)
        productos = list(carrito.find())  # Convertir el cursor en una lista de productos

        if posicion >= 0 and posicion < len(productos)+1:
            producto_eliminar = productos[posicion - 1]
            id_producto = producto_eliminar['id']

            self.mongo_helper.delete_document(self.collection,id_producto)
            print("Producto eliminado del carrito.")
        else:
            print("Posición inválida.")

    def getItems(self):
        carrito = self.mongo_helper.get_documents(self.collection)
        return carrito

    def mostrarCarrito(self):
        carrito = self.mongo_helper.get_documents(self.collection)
        print("+" + " Carrito ".center(65, "-") + "+")
        print("| " + "ID PRODUCTO | DESCRIPCIÓN          | CANTIDAD | PRECIO UNITARIO" + " |")  # header
        i = 0
        for producto in carrito:
            i += 1
            id = producto['id']
            nombre = producto['nombre']
            cantidad = producto['cantidad']
            precio = producto['precio']
            print("| " + f"{i}.ID:{id: <6} | {nombre: <20} | " + f"(x{cantidad})".ljust(8) + " | " + f"${precio} c/u".rjust(15) + " |")
        print("+" + "-" * 65 + "+")

    def calcular_impuestos(self, total_items):
        impuestos = total_items * 0.21  # 21% de impuestos IVA
        return impuestos

    def calcular_descuento(self, cliente, total_items):
        tiempo_promedio = cliente['tiempo_promedio']
        if tiempo_promedio > 240:
            porcentaje_descuento = 40
            tipo_descuento = "Usuario TOP"
        elif tiempo_promedio > 120:
            porcentaje_descuento = 20
            tipo_descuento = "Usuario MEDIUM"
        else:
            porcentaje_descuento = 10
            tipo_descuento = "Usuario LOW"

        importe_descuento = porcentaje_descuento * 0.01 * total_items
        return tipo_descuento, porcentaje_descuento, importe_descuento

    def total_items(self, carrito):
        # Calcular el total de items del carrito
        total_carrito = 0
        for i in carrito:
            total_carrito += (i['cantidad'] * i['precio'])
        return total_carrito

    def calcular_importe_total(self, carrito, impuestos, importe_descuento):
        total_carrito = 0
        for i in carrito:
            total_carrito += (i['cantidad'] * i['precio'])
        total_carrito = total_carrito + impuestos - importe_descuento
        return total_carrito

    def insertar_datos_cassandra(self, carrito):
        self.cassandra_helper.conectar()  # Conexión a Cassandra
        self.cassandra_helper.usar_db('BDD')  # Utilizar el keyspace 'BDD'

        for producto in carrito:
            # Insertar los datos del producto en la tabla
            columns = ["producto", "descripcion", "fecha_compra", "precio_unitario"]
            values = [f"'{producto['nombre']}'", f"'{producto['descripcion']}'", "toTimestamp(now())",
                      str(producto['precio'])]
            self.cassandra_helper.insert_document("compras", columns, values)

        self.cassandra_helper.close_connection()  # Cerrar la conexión a Cassandra
