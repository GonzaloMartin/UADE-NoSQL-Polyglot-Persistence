from controllers.mongo_hlp import *

class LoginHLP:
    def __init__(self):
        self._mongoHLP = MongoHelper()
        self._mongoHLP.conectar()
        self._mongoHLP.usar_db('bdd2')

    def login(self, username, password):
        # Aquí puedes agregar lógica de validación y autenticación
        query = {
            'user': username,
            'password': password
        }
        result = self._mongoHLP.get_collection('usuarios').find_one(query)

        if result is None:
            print("Invalid username or password.")
        else:
            print("Login successful!")

    def register(self, username, password, dni, address):
        # Aquí puedes agregar lógica de validación y creación de usuarios
        success = self.database.create_user(username, password, dni, address)
        if success:
            print("Registration successful!")
        else:
            print("Registration failed.")
