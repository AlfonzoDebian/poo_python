# POO en Python

- El paradigma de poo esta basado en una abstraciòn del mundo real que nos va permitir desarrollar programar de forma mas cercana de como vemos el mundo. pensando el objeto que tengo mas adelante y acciones que podemos hacer con ellos.


## Clase 

- Una clase es un tipo de dato, cuya variables, se llaman objetos o instancias.

- La clase es la difinicion del contexti del mundo real y los objetos son instancias. Son el propio objeto del mundo real.

- Las clases estan compuesta por 2 elementos, atributos y metodos.

### Atributos 

- Informacion que almacena la clase.

### Metodos 

- Las operaciones que pueden realizar las clases

## Definicion de una clase en python

```Python
class NombresClase:

 def __init_(self, variable, variable2):
  self.Atributo1 = valor1
  self.Atributo2 = valor2


def nombreMetodoself(self):
    bloqueCodigo
```
### Componentes

```class```: palabra reservada en python para defininir una clase

```NombreClase```: Nombre de la clase que quieres crear.

```def```: Palabra reservada en python que se usa para definir tanto el constructor de la clase (metodo que se ejecuta a la primera vez que usas una clase) como los diferente metodos que tiene.

```___init____```: Nombre del ```def``` para la funcion.

```(self, x)```: Para metro del constructor de la clase. El parametro self es obligatorio y despues puede tener tantos parametros cuando quieras. La forma de medir parametros es la misma que en las funciones.

```self.AtributosX```: forma de utilizacion y acceso a los atributos de la clase. 

```NombreMetodo```: nombre metodo de la clase-.


```self```: Parametro del metodo, Y despues puede poner el parametro que quieras 

```bloaud codigo```: Intrucciones que ejecutaran el metodo.

- Cuando define una clase debe tener en cuenta los siguentes puntos:
   - Puedes definir tantos atributos como necesites.
   - Puedes definir tantos metodos como necesite.
   - Puede definir tantos parametros como en el contructor y tantos metodos que necesites.

## Compisicion
- Consiste en la creacion de nuevas clases a partir de otras clases ya existente que actuan como elementos compositores de la nueva.
- Las clases existente seran atributos de la nuevas clases.
- En ```POO```la composicion significa que entre las 2 clases existe una relacion de tipo ```1```
- Ejemplo:
    - Una cordenadaa en dos dimesiones esta compuesta por 2 valores. el valor en el eje de la x y el valor en el eje de la y, esto podria ser una clase.Un cuadrado esta compuesto por 4 cordenadas, que son los 4 vertices, esto podria ser una clase que esta compuesta por 4 clases de los objeto cordenada.

