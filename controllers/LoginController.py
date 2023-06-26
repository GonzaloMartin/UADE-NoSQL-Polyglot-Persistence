import sys
from controllers.mongo_hlp import *
from all_classes.clases import Usuario

sys.path.append("../../..")

class LoginHLP:
    def __init__(self):
        self._mongoHLP = MongoHelper()
        self._mongoHLP.conectar()
        self._mongoHLP.usar_db('bdd2')

    def login(self, username, password):
        # Aquí puedes agregar lógica de validación y autenticación
        query = {
            'name': username,
            'password': password
        }
        result = self._mongoHLP.get_collection('usuarios').find_one(query)
        try:
            if  result['name'] == query['name'] and result['password'] == query['password']:
                print("Inicio de sesión exitoso")
                usuario = Usuario(result)  #setea todos los valores al objeto usuario que se encuentran en la BDD
                return usuario
            else:
                print("Invalid username or password") #de momento no entra nunca acá, siempre sale el error NoneType is not subscriptable
                return None
        except Exception as err:
                print("Usuario no encontrado, intente nuevamente")
                return None


    def register(self, username, password, dni, address):
        # Aquí puedes agregar lógica de validación y creación de usuarios
        success = self.database.create_user(username, password, dni, address)
        if success:
            print("Registration successful!")
        else:
            print("Registration failed.")
