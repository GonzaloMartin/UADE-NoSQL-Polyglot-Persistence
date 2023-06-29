import sys
from controllers.mongo_hlp import *
from all_classes.clases import Usuario

sys.path.append("../../..")

class usuario_controller:
    def __init__(self):
        self._mongoHLP = MongoHelper()
        self._mongoHLP.conectar()
        self._mongoHLP.usar_db('bdd2')
        self.collection = 'usuarios'
        self.query = {}


    def login(self, username, password):
        # Aquí puedes agregar lógica de validación y autenticación
        self.query = {
            'name': username,
            'password': password
        }
        result = self.getUser()
        try:
            if  result is not None:
                print("Inicio de sesión exitoso")
                usuario = Usuario(result)  #setea todos los valores al objeto usuario que se encuentran en la BDD
                return usuario
            else:
                print("Invalid username or password") #de momento no entra nunca acá, siempre sale el error NoneType is not subscriptable
                return None
        except Exception as err:
                print("Usuario no encontrado, intente nuevamente: ",err)
                return None

    def getUser(self):
        return self._mongoHLP.get_document_by_name(self.collection,self.query)


    def register(self, username, password, dni, address):
        # Aquí puedes agregar lógica de validación y creación de usuarios
        success = self.database.create_user(username, password, dni, address)
        if success:
            print("Registration successful!")
        else:
            print("Registration failed.")
