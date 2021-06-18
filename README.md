# ParcialHerramientasComputacionales

# ¿Que problema es?
El problema al que se da solucion en el archivo "*parcial final.py*", es un problema en el cual se quiere reactivar las cafeterias de una universidad y para esto se van a aplicar una serie de descuentos dependiendo de si el usuario es estudiante o profesor los descuentos que se aplican son los **Sgtes**:

* Los estudiantes tienen un 50%.
* Los profesores tienen un 20%.

Al final el programa debe mostrar en pantalla la Sgte información:

* ”El **Rol** con **cedula Numero**, debe pagar **Valor** por el producto **Codigo**”.

Para la solución de este archivo se aplica el sgte **modelo computacional**:

# Entradas
Las entradas que recibira el programa son las sgtes:

* La accion que desea realizar el usuario a manera de numero.
* El numero de cedula del usuario.
* La opcion a forma de numero correspondiente al Rol.
* Luego el codigo del producto que desea comprar.
* Luego la cantidad de producto que desea comprar.

### En caso que se quiera registrar un producto:

* Nombre del producto que desea registar.
* El codigo del nuevo producto.
* el precio del nuevo producto.

# Proceso para comprar producto
### Paso 1: 
Se evalua si el **rol** ingresado es correcto.

### Paso 2:
Luego se evalua si el **codigo del producto** existe.

### Paso 3:
Se calcula el **precio** segun la cantidad y se aplica el descuento.

# Proceso para registrar producto

### Paso 1:
Se evalua si el **codigo** ya existe.

### Paso 2: 
En caso de que el **codigo de producto** ya exista se le imprime una mensaje al usuario. y en caso de que no exista se agrega a una lista y esta se agrega a la **matriz**.

# Salidas
Como salidas tenemos las sgtes:
1. Para el caso de compra de producto:
  * ”El **Rol** con **cedula Numero**, debe pagar **Valor** por el producto **Codigo**”.
2. Para el caso de registro de producto:
  * La Matriz actualizada.
  * o el mensaje de error en caso que el codigo ya exista.




