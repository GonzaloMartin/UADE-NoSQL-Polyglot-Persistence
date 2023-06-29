from controllers.mongo_hlp import MongoHelper
from all_classes.clases import Producto

class catalogo_productos:
    def __init__(self):
        self.mongo_helper = MongoHelper()
        self.mongo_helper.conectar()
        self.mongo_helper.usar_db('bdd2')
        self.collection = 'productos'

    #devuelve el todos los documentos que macheen en el nombre 'producto'
    def buscar(self, nombre_producto):
        nombre_producto = nombre_producto.lower()
        resultados = self.mongo_helper.get_matching_documents(self.collection,"nombre",nombre_producto)
        return resultados

    def mostrar_catalogo(self,catalogo):
        print("Resultados de búsqueda:")
        for i, prod in enumerate(catalogo):
            print(f"{i + 1}. {prod['nombre']} ${prod['precio']}")
            print("-----------------------")
        catalogo.rewind()

    def seleccionar_producto(self,seleccion,catalogo):
        documento = catalogo[seleccion - 1]
        producto = Producto(documento['id'],documento['nombre'],documento['precio'],0,documento['categoria'],documento['descripcion'])
        return producto

