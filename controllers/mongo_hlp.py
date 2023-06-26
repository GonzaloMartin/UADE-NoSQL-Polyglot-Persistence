# Para levantar mongo desde docker tipear mongosh
from pymongo import MongoClient

class MongoHelper:
    def __init__(self):
        self._client = None
        self._db = None

    def conectar(self, port='mongodb://127.0.0.1:27017/'):
        self._client = MongoClient(port)

    def usar_db(self, db_name):
        self._db = self._client[db_name]

    def get_collection(self, collection_name):
        return self._db[collection_name]

    def get_documents(self,collection):
        coleccion = self._db[collection]
        return list(coleccion.find())

    def insert_document(self,collection,document):
        coleccion = self._db[collection]
        coleccion.insert_one(document)

    #def update_document(self, filter, update):
        #self._collection.update_one(filter, update)

    def close_connection(self):
        if self._client:
            self._client.close()

    def get_client(self):
        return self._client
    
    #def check_user():
        






"""
cliente=MongoClient
#para obtener una colección
def conectarMongo():
    try:
        client = MongoClient('mongodb://127.0.0.1:27017/')
        return client
    except Exception as e:
        print(e)

def setClient(client):
    cliente=client

def getClient():
    return cliente

def getColeccion(client,base,coleccion):
    try:
        conectarMongo()
        db = client[base]#'bdd2'
        # Accede a una colección en la base de datos
        collection = db[coleccion] #'usuarios'
        return collection
    except Exception as e:
        print(e)

def setDocumento(documento,collection):
    try:
        result = collection.insert_one(documento)
        return result.inserted_id
    except Exception as e:
        print("Error al insertar documento. Error: "+e)
    
def getDocumento(client,base,collection):
    getColeccion(client,base,collection)
    documents = collection.find()



nuevo_documento = {
    "nombre": "Lenovo",
    "apellido": "ThinkPad"
}

# Inserta el nuevo documento en la colección
result = collection.insert_one(nuevo_documento)

# Imprime el ID del documento recién insertado
print("Documento insertado. ID:", result.inserted_id)

# Realiza operaciones en la colección, por ejemplo, obtén los documentos
documents = collection.find()

documents = collection.find({}, {"nombre": 1})

# Itera sobre los documentos e imprime la marca
for document in documents:
    print(document["nombre"])"""

