from controllers.mongo_hlp import MongoHelper
from all_classes.clases import Carrito

class carrito_controller:
    def __init__(self):
        self.mongo_helper = MongoHelper()
        self.mongo_helper.conectar()
        self.mongo_helper.usar_db('bdd2')
        self.collection = "carrito"

    def existeCarrito(self):
        return self.mongo_helper.exists_documents(self.collection)

    def existeProductoEnCarrito(self,prod):
        return self.mongo_helper.get_document_by_id(self.collection,prod.id)


    def agregarProducto(self,producto):
        try:
            if self.existeCarrito() is None or (self.existeCarrito() and self.existeProductoEnCarrito(producto) is None):
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
                print("Agregado al carrito!")
            else:
                try:
                    # Realizar la actualización
                    doc = self.mongo_helper.get_document_by_id(self.collection,producto.id)
                    cantidadActual = doc['cantidad']
                    query = (
                        {'$set': {'cantidad': cantidadActual + producto.cantidad}}
                    )
                    self.mongo_helper.update_document(self.collection,producto.id,query)
                    print('Actualización exitosa.')
                except Exception as e:
                    print('Error al actualizar la cantidad:', e)
        except Exception as e:
            print("se a producido un error a la hora de cargar el producto al carrito:",e)

    def mostrarCarrito(self):
        carrito = self.mongo_helper.get_documents(self.collection)
        print("\n -----     carrito     -----\n")
        for producto in carrito:
            nombre = producto['nombre']
            cantidad = producto['cantidad']
            precio = producto['precio']
            print(f"{nombre} ({cantidad}) ${precio} c/u")




