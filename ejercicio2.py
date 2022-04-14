class Modelo():
    def __init__(self, texto):
        self.texto = texto
    
class Vista():
    def __init__(self):
        self.modelo = Modelo(input("Introduce un texto: "))
    
    def mayusculas(self):
        print(self.modelo.texto.upper())
        
class Controlador():
    def __init__(self):
        self.vista = Vista()
    
    def get_textomayusculas(self):
        self.vista.mayusculas()
        
class Cliente():
    controlador = Controlador()
    controlador.get_textomayusculas()
Cliente()