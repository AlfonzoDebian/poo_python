# Herencia Múltiple en Python

Este repositorio contiene ejemplos para demostrar el concepto de herencia múltiple en Python.

## ¿Qué es la Herencia Múltiple?

La herencia múltiple es una característica de Python que permite a una clase heredar atributos y métodos de múltiples clases padre. Esto permite combinar funcionalidades de diversas fuentes en una sola clase hija.

## Ejemplos

### Ejemplo Básico

```Python

class Animal:
    def hablar(self):
        print("El animal hace un sonido.")

class Mamifero:
    def caminar(self):
        print("El mamífero está caminando.")

# La clase q va hacer la herencia 
class Perro(Animal, Mamifero):
    def ladrar(self):
        print("¡Guau!")

# aca creo una instancia Xd
perrito = Perro()

# Aca empiezo a heredar
perrito.hablar()  
perrito.caminar()  
perrito.ladrar() 