#redis-cli
import redis

import redis

class RedisHelper:
    def __init__(self):
        self._client = None

    def connect(self, host='localhost', port=6379):
        self._client = redis.Redis(host=host, port=port)

    def set_value(self, key, value):
        self._client.set(key, value)

    def get_value(self, key):
        return self._client.get(key).decode() #decode le saca la b inicial.

    def delete_key(self, key):
        self._client.delete(key)

    def close_connection(self):
        self._client.close()


