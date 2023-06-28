#cqlsh para arrancar cassandra
from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthProvider

#en cassandra keyspace = BDD

class CassandraHelper:
    def __init__(self):
        self._cluster = None
        self._session = None
        self._keyspace = None

    def conectar(self):
        self._cluster = Cluster(['127.0.0.1','7000'])
        self._session = self._cluster.connect()

    def usar_db(self, keyspace):
        self._session.set_keyspace(keyspace)

    #obtener bdd actual
    def getKeyspace(self):
        return self._session.keyspace()

    def execute_query(self, query):
        return self._session.execute(query)

    def get_all_documents(self, table):
        query = f"SELECT * FROM {table}"
        result = self.execute_query(query)
        return list(result)

    def insert_document(self, table, columns, values):
        query = f"INSERT INTO {table} ({', '.join(columns)}) VALUES ({', '.join(values)})"
        self.execute_query(query)

    def update_document(self, table, set_values, where_clause):
        query = f"UPDATE {table} SET {set_values} WHERE {where_clause}"
        self.execute_query(query)

    def close_connection(self):
        self._session.shutdown()
        self._cluster.shutdown()
