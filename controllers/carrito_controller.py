from controllers.mongo_hlp import MongoHelper
from all_classes.clases import Carrito

class carrito_controller:
    def __init__(self):
        self.mongo_helper = MongoHelper()
        self.mongo_helper.conectar()
        self.mongo_helper.usar_db('bdd2')
        self.collection = "carrito"
        self.carrito = None

    def existeCarrito(self):
        return self.mongo_helper.exists_documents(self.collection)

    def agregarProducto(self,producto):
        try:
            if self.existeCarrito() is None:
                #se agrega el producto
                query = {
                    'id': producto.id,
                    'nombre': producto.nombre,
                    'precio': producto.precio,
                    'cantidad': producto.cantidad,
                    'categoria': producto.categoria,
                    'descripcion': producto.descripcion
                }
                self.mongo_helper.insert_document('carrito',query)
                carrito = Carrito()
                carrito.agregar_producto(producto)
                self.carrito = carrito
            else:
                try:
                    # Realizar la actualización
                    query = (
                        {'_id': producto.id},
                        {'$set': {'cantidad': producto.cantidad}}
                    )
                    self.mongo_helper.update_document(query)
                    print('Actualización exitosa.')
                except Exception as e:
                    print('Error al actualizar la cantidad:', e)
                self.carrito.agregar_producto(producto)
        except Exception as e:
            print("se a producido un error a la hora de cargar el producto al carrito:",e)

    def mostrarCarrito(self):
        self.carrito.mostrar_carrito()




