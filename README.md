# BDD2
instalaciones:

pip install cassandra-driver
pip install pymongo
pip install redis (tambien instalar el comprimido de redis desde https://redis.io/download/)

--- ejemplo de carga de un nuevo usuario
db.usuarios.insertOne({name:"Federico",password:"fede123",address:"Av Rivadavia 123",dni:"41758077",tiempo_promedio:130,condicionImpuestos:0})
