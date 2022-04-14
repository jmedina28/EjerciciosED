<h1 align="center">Estructuras de datos</h1>

<h3 align="center">Autor de este proyecto:</h3>

1. [@jmedina28](https://github.com/jmedina28)
---
En este [repositorio](https://github.com/jmedina28/EjerciciosED) quedan resuelto el ejercicio de estructuras de datos para POO. Para llevar a cabo el proyecto me he documentado a través de la teoría que se encuentra en el campus virtual y de diversas fuentes que he encontrado.
***
## Ejercicio 1

En este ejercicio he completado las clases que estaban creadas y he creado la función visitante la cual recorre el programa.

El código empleado para resolverlo es el siguiente: 

```python
class Bloque:
    # Un bloque es un conjunto de instrucciones ejecutadas
    # unas detrás de otras.
    def __init__(self):
        # Por defecto, un bloque no contiene ninguna instrucción.
        self.instrucciones = []

    def agregarInstruction(self, instruccion):
        self.instrucciones.append(instruccion)


class Si:
    # Representa una instrucción 'if'. 'condicion' es una cadena
    # de caracteres que contiene la evaluación de la condición,
    # 'entonces' es el bloque de instrucciones ejecutadas si la condición
    # se verifica, 'si_no' es el bloque de instrucciones ejecutadas
    # si no se verifica.

    def __init__(self, condicion, entonces, si_no):
        self.condicion = condicion
        self.entonces = entonces
        self.si_no = si_no

    def ejecutar(self):
        entonces = self.entonces
        si_no = self.si_no

        if self.condicion == True:
            Mostrar(entonces).mostrar()
        else:
            Mostrar(si_no).mostrar()


class MientrasQue:
    # Representa una instrucción 'while'.
    # 'condicion' es una cadena que contiene el valor evaluado
    # para decidir si el bucle continúa o no,
    # 'bloque' es la secuencia de instrucciones ejecutadas en bucle.
    def __init__(self, condicion, bloque):
        self.condicion = condicion
        self.bloque = bloque

    def bucle(self):
        variable1 = 1
        while variable1 <= self.condicion:
            Mostrar(self.bloque).mostrar()
            variable1 += 1


class Mostrar:
    # Una instrucción para mostrar un mensaje
    # en salida estándar.
    def __init__(self, mensaje):
        self.mensaje = mensaje

    def mostrar(self):
        print(self.mensaje)


def visitante(variable_visitante):

    if variable_visitante == 1:
        mostrar_ok = "OK"
        mostrar_ko = "KO"
        alternativa = Si(2+2 == 4, mostrar_ok, mostrar_ko)
        alternativa.ejecutar()
    elif variable_visitante == 2:
        alternativa = MientrasQue(int(input("Introduzca cuántas veces desea que se repita el bucle: ")), input(
            "Introduzca el texto que desea ejecutar en bucle:"))
        alternativa.bucle()
    else:
        print("Introduzca valores correctos por favor.")
        visitante(input(
            "Si desea ejecutar el ejemplo del enunciado pulse 1, en cambio si desea probar el bucle de la clase MientrasQue pulse 2: "))
```
## Ejercicio 2

En este ejercicio he aplicado MVC para generar un archivo que devuelva una cadena de texto introducida en mayúsculas.

El código empleado para resolverlo es el siguiente:

```python
import os
import time

class Modelo():
    def __init__(self, texto):
        self.texto = texto
    
class Vista():
    def __init__(self):
        self.modelo = Modelo(input("Introduce un texto: "))
    
    def mayusculas(self):
        fichero = open("Mayus.txt", "a")
        fichero.write(self.modelo.texto.upper())
        fichero.close()
        time.sleep(20)
        os.remove("Mayus.txt")
class Controlador():
    def __init__(self):
        self.vista = Vista()
    
    def get_textomayusculas(self):
        self.vista.mayusculas()
        
class Cliente():
    controlador = Controlador()
    controlador.get_textomayusculas()
Cliente()
```
## Ejercicio 3

En este ejercicio he desarrollado el código tal y como se pedía para que tuviera un funcionamiento concreto.

El código empleado para resolverlo es el siguiente:

```python
"""Comportamiento esperado:

producto = Producto(Naturaleza.ALIMENTARIA) # IVA 5,5% 
precio_neto = FactoryFactura.crear(producto).facturar() 
print(precio_neto) 
# 105.5 
 
producto = Producto(Naturaleza.SERVICIO) # IVA 20% 
precio_neto = FactoryFactura.crear(producto).facturar() 
print(precio_neto) 
# 120 
"""


class Naturaleza:
   ALIMENTARIA = 0.055
   SERVICIO = 0.2


class FactoryFactura:
   class crear():
       def __init__(self, tipo_producto):
           self.tipo_producto = tipo_producto

       def facturar(self):
           if self.tipo_producto == 0.2 or 0.05:
               self.precio = 100
               return self.precio+(self.precio*self.tipo_producto)
           else:
               print("Solo se pueden facturar servicios o productos alimentarios.")


def Producto(IVA):
   return IVA


producto = Producto(Naturaleza.ALIMENTARIA)
precio_neto = FactoryFactura.crear(producto).facturar()
print(precio_neto)

producto = Producto(Naturaleza.SERVICIO)
precio_neto = FactoryFactura.crear(producto).facturar()
print(precio_neto)
```
