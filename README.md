# BDD2
instalaciones:

pip install cassandra-driver
pip install pymongo
pip install redis (tambien instalar el comprimido de redis desde https://redis.io/download/)

--- ejemplo de carga de un nuevo usuario
db.usuarios.insertOne({name:"Federico",password:"fede123",address:"Av Rivadavia 123",dni:"41758077",tiempo_promedio:130,condicionImpuestos:0})

--ejemplo crear productos
db.productos.insertMany([{id: 001, nombre: "Remera Adidas", precio: 150.00, categoria: "Indumentaria", descripcion: "Es una remera de algodón de color rojo."},{id: 002, nombre: "Zapatillas Adidas", precio: 320.00, categoria: "Calzado", descripcion: "Las mejores zapatillas, maximo confort."}, {id: 003, nombre: "Pantalon Adidas", precio: 40.00, categoria: "Indumentaria", descripcion: "Pantalon joggin de color negro."}])
