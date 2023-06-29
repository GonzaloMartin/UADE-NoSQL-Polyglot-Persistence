from controllers.cassandra_hlp import CassandraHelper

class ConfirmarCarrito:
    def __init__(self):
        self.cassandra_helper = CassandraHelper()

    def calcular_impuestos(self, carrito):
        total_carrito = sum(item['cantidad'] * item['precio_unitario'] for item in carrito)
        impuestos = total_carrito * 0.21  # 21% de impuestos IVA
        return impuestos

    def calcular_descuento(self, cliente, carrito):
        tiempo_promedio = cliente['tiempo_promedio']
        if tiempo_promedio > 240:
            porcentaje_descuento = 40
            tipo_descuento = "Usuario TOP"
        elif tiempo_promedio > 120:
            porcentaje_descuento = 20
            tipo_descuento = "Usuario MEDIUM"
        else:
            porcentaje_descuento = 10
            tipo_descuento = "Usuario LOW"

        importe_descuento = porcentaje_descuento * 0.01 * sum(item['cantidad'] * item['precio_unitario'] for item in carrito)
        return tipo_descuento, porcentaje_descuento, importe_descuento

    def calcular_importe_total(self, carrito, impuestos, importe_descuento):
        total_carrito = sum(item['cantidad'] * item['precio_unitario'] for item in carrito)
        importe_total = total_carrito + impuestos - importe_descuento
        return importe_total

    def insertar_datos_cassandra(self, carrito):
        self.cassandra_helper.conectar()  # Conexión a Cassandra
        self.cassandra_helper.usar_db('BDD')  # Utilizar el keyspace 'BDD'

        for producto in carrito:
            # Insertar los datos del producto en la tabla
            columns = ["producto", "descripcion", "fecha_compra", "precio_unitario"]
            values = [f"'{producto['nombre']}'", f"'{producto['descripcion']}'", "toTimestamp(now())",
                      str(producto['precio'])]
            self.cassandra_helper.insert_document("compras", columns, values)

        self.cassandra_helper.close_connection()  # Cerrar la conexión a Cassandra
