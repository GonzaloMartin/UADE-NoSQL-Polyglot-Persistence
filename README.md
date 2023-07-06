# **Ingeniería de Datos 2 - Persistencia Políglota**

## Tabla de Contenidos
- [**Ingeniería de Datos 2 - Persistencia Políglota**](#ingeniería-de-datos-2---persistencia-políglota)
  - [Tabla de Contenidos](#tabla-de-contenidos)
  - [Introducción](#introducción)
  - [Secciones de la aplicación](#secciones-de-la-aplicación)
    - [**LOGIN**](#login)
    - [**BUSCAR PRODUCTOS**](#buscar-productos)
    - [**GESTIONAR CARRITO**](#gestionar-carrito)
    - [**CONFIRMAR COMPRA**](#confirmar-compra)
  - [Comandos necesarios para la ejecución de la aplicación](#comandos-necesarios-para-la-ejecución-de-la-aplicación)
    - [*Comando para **Crear un Usuario***](#comando-para-crear-un-usuario)
    - [*Comando para crear un **Catálogo de Productos***](#comando-para-crear-un-catálogo-de-productos)
  - [Repositorio de la aplicación](#repositorio-de-la-aplicación)
  - [Equipo de Trabajo](#equipo-de-trabajo)
  - [Profesor](#profesor)

## Introducción
La aplicación se enfoca sobre la gestión de creación de pedidos teniendo en cuenta aspectos como la validación de los datos del cliente, la creación de productos, el estado del carrito de compras y el proceso de pago y registro de las compras.

Las bases de datos utilizadas para el desarrollo de la aplicación fueron ***MongoDB***, ***Redis*** y ***Cassandra***.

## Secciones de la aplicación
### **LOGIN**
En esta sección se controla el ingreso de un usuario a la aplicación, ya sea un cliente o un administrador, aquí se registrarán datos como Usuario, Contraseña, Dirección, Documento y Tipo de usuario. 

Para lograr conservar estos datos utilizaremos **MongoDB**, una base de datos ideal gracias a su flexibilidad en el modelado de datos, su alta disponibilidad y escalabilidad; ya que se precisa acceder siempre a estos datos e incluso otros datos como la contraseña, la dirección o el tipo de usuario pueden ser modificados.

En cuanto al tiempo de actividad, lo registraremos utilizando **Redis**, una base de datos que dispone de características como la alta disponibilidad, almacenamiento en memoria (lo cual brinda un acceso rápido a la información) y otras como el TTL (time to live). Lo cual permite categorizar al usuario y asignar beneficios de manera eficiente.

### **BUSCAR PRODUCTOS**
Al momento de la búsqueda de productos, previamentes cargados en un Catálogo de Productos, y de sumarlos al carrito, aquí decidimos utilizar **MongoDB** debido a que proporciona consultas capaces de filtrar productos en función de múltiples criterios y en caso de extenderse el listado de productos Mongo proporciona escalabilidad suficiente para manejar grandes volúmenes de datos y garantizar un rendimiento óptimo de los mismos.

Además, al utilizar una base de datos NoSQL basada en documentos, no requiere un esquema fijo predefinido, por lo tanto, nos proporciona flexibilidad y escalabilidad permitiendo almacenar información en documentos de forma no estructurada.

### **GESTIONAR CARRITO**
En esta sección de la aplicación se realizan las tareas necesarias para gestionar un carrito existente, listarlo o confirmarlo. Aquí nuevamente nos decantamos por **MongoDB** ya que los datos del carrito se encuentran registrados en esta base de datos, por lo que nos permite actualizarlo de manera optima o listarlo de una forma mas sencilla en el código.

Tambien aqui se guardan los estados anteriores del carrito, recordando el Id del producto y su cantidad. Se suman a estos datos el "index" para poder recorrer todos los productos y una variable "estado_anterior" para saber si ya se volvio o no al estado anterior del carrito, ya que solo se permite volver atras una sola vez. Aqui utilizamos Redis nuevamente, lo que nos permitira volver a estados anteriores con rapidez y tambien tener alta disponibilidad, y la posibilidad de escalar.

### **CONFIRMAR COMPRA**
En ultimo lugar, la funcionalidad del sistema concluye con la confirmación de la compra. Aquí utilizamos **Cassandra** para conservar los datos debido a su escalabilidad lineal, ya que el volumen de facturas puede crecer exponencialmente con el tiempo. Su modelo de datos basado en columnas permite diseñar el esquema de manera tal que se ajuste a la estructura de una factura.

Por otro lado, también se utilizó **Cassandra** ya que posee una baja latencia y es una base de datos de rápida en su respuesta, ideal a la hora de generar y mostrar al cliente los detalles de su factura.

## Comandos necesarios para la ejecución de la aplicación
```console
pip install cassandra-driver
pip install pymongo
pip install redis (tambien instalar el comprimido de redis desde https://redis.io/download/)
```


### *Comando para **Crear un Usuario***
```console
Primero configuramos MongoDB

use bdd2

Output esperado:
switched to db bdd2
```
Luego creamos el usuario
```console


db.usuarios.insertOne({name:"Juan",password:"juan123",address:"Av Rivadavia 123",dni:"40751234",tiempo_promedio:130,condicionImpuestos:0})

Output esperado:
{
  acknowledged: true,
  insertedId: ObjectId("64a3c477b2b10f2cae987d68")
}
```

### *Comando para crear un **Catálogo de Productos***
```console
db.productos.insertMany([
  {id: 004, nombre: "Pelota de Futbol", precio: 80.00, categoria: "Deportes", descripcion: "Pelota de futbol de tamaño estándar."},
  {id: 005, nombre: "Campera deportiva Adidas", precio: 420.00, categoria: "Indumentaria", descripcion: "Campera deportiva de Adidas, ideal para actividades al aire libre."},
  {id: 006, nombre: "Camiseta Argentina 3 Estrellas", precio: 230.00, categoria: "Indumentaria", descripcion: "Camiseta oficial de la selección Argentina con 3 estrellas."},
  {id: 007, nombre: "Guantes de Boxeo Everlast", precio: 120.00, categoria: "Deportes", descripcion: "Guantes de boxeo profesionales marca Everlast."},
  {id: 008, nombre: "Pelota de Basket", precio: 70.00, categoria: "Deportes", descripcion: "Pelota de basket de tamaño estándar."},
  {id: 009, nombre: "Bicicleta", precio: 900.00, categoria: "Deportes", descripcion: "Bicicleta de montaña de alta calidad."},
  {id: 010, nombre: "Monopatin", precio: 1500.00, categoria: "Deportes", descripcion: "Monopatin para uso recreativo y de transporte urbano."}
]);

Output esperado:
{
  acknowledged: true,
  insertedIds: {
    '0': ObjectId("64a3c564b2b10f2cae987d69"),
    '1': ObjectId("64a3c564b2b10f2cae987d6a"),
    '2': ObjectId("64a3c564b2b10f2cae987d6b"),
    '3': ObjectId("64a3c564b2b10f2cae987d6c"),
    '4': ObjectId("64a3c564b2b10f2cae987d6d"),
    '5': ObjectId("64a3c564b2b10f2cae987d6e"),
    '6': ObjectId("64a3c564b2b10f2cae987d6f"),
    '7': ObjectId("64a3c564b2b10f2cae987d70"),
    '8': ObjectId("64a3c564b2b10f2cae987d71"),
    '9': ObjectId("64a3c564b2b10f2cae987d72")
  }
}


```



### *Comando para **Configurar Cassandra***
```console
Creacíon de la KeySpace:
create KEYSPACE BDD WITH replication = {'class': 'SimpleStrategy', 'replication_factor': '1' };
use BDD;
```

## Repositorio de la aplicación
>GitHub del proyecto: https://github.com/federey99/BDD2.git

## Equipo de Trabajo
- Palombo Agustín – LU: 1098394
- Montalvo Gonzalo Martín – LU: 1142004
- Sánchez Agüero, Franco – LU: 1115176
- Rey, Federico Gabriel – LU: 1117866 

## Profesor
-	Godio, Claudio José


