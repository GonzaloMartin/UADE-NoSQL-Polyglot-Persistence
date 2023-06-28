from controllers.mongo_hlp import MongoHelper

class BuscarProducto:
    def __init__(self):
        self.mongo_helper = MongoHelper()
        self.mongo_helper.conectar()
        self.mongo_helper.usar_db('bdd2')

    def buscar_producto(self, producto, collection):
        productos = self.mongo_helper.get_documents(collection)

        resultados = []
        for prod in productos:
            if producto.lower() in prod['nombre'].lower():
                resultados.append(prod)

        return resultados


