from controllers.cassandra_hlp import *
from controllers.mongo_hlp import *
from controllers.redis_hlp import *

# Uso del controlador MONGO
mongo_helper = MongoHelper()
mongo_helper.conectar()
mongo_helper.usar_db('bdd2')
#mongo_helper.get_collection('usuarios')
#mongo_helper.get('mycollection')

# Insertar un documento
document = {'name': 'John Doe', 'age': 30}
mongo_helper.insert_document('usuarios',document)

# Obtener todos los documentos de la colección
documents = mongo_helper.get_documents('usuarios')
for doc in documents:
    print(doc)

# Cerrar la conexión
mongo_helper.close_connection()



# Uso del controlador CASSANDRA
cassandra_helper = CassandraHelper()
cassandra_helper.connect()
cassandra_helper.set_keyspace('my_keyspace')

# Insertar un documento
columns = ['name', 'age']
values = ["'John Doe'", '30']
cassandra_helper.insert_document('my_table', columns, values)

# Obtener todos los documentos de la tabla
documents = cassandra_helper.get_all_documents('my_table')
for doc in documents:
    print(doc)

# Cerrar la conexión
cassandra_helper.close_connection()


# Uso del controlador REDIS
redis_helper = RedisHelper()
redis_helper.connect()

# Setear un valor
redis_helper.set_value('clave', 'valor')

# Obtener un valor
valor = redis_helper.get_value('clave')
print(valor)

# Eliminar una clave
redis_helper.delete_key('clave')

# Cerrar la conexión
redis_helper.close_connection()
