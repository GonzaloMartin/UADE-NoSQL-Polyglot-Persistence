from cassandra_hlp import *
from mongo_hlp import *
from redis_hlp import *

# Uso del controlador MONGO
mongo_helper = MongoHelper()
mongo_helper.conectar()
mongo_helper.usar_db('bdd2')

# Insertar un documento
#document = {'name': 'John Doe', 'age': 30}
#mongo_helper.insert_document('usuarios',document)

 # Ignorar mayúsculas y minúsculas

# Realizar la búsqueda utilizando la expresión regular
#result = mongo_helper["productos"].find({"nombre": {"$regex": "adidas", "$options": "i"}})
result = mongo_helper.get_matching_documents('productos',"nombre","adidas")
print(result)
print(result[2])
print(result[2]['nombre'])
#result = mongo_helper.exists_documents('a')
#print(result)

#fede2 = result['tiempo_promedio']

#print(type(fede2),fede2)




# Obtener todos los documentos de la colección
#documents = mongo_helper.get_documents('usuarios')
#for doc in documents:
#    print(doc)

# Cerrar la conexión
"""
mongo_helper.close_connection()



# Uso del controlador REDIS
redis_helper = RedisHelper()
redis_helper.connect()

# Setear un valor
redis_helper.set_value('usuario:2', fede2)

# Obtener un valor
valor = redis_helper.get_value('usuario:2')
print(valor,"reddis")

# Eliminar una clave
#redis_helper.delete_key('clave')

# Cerrar la conexión
redis_helper.close_connection()



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

"""