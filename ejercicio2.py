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