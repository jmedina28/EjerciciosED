class Modelo():
    def __init__(self):
        self.texto = "Hola, me llamo Juan Antonio y necesito que me devuelvas este texto en mayúsculas."
    
class Vista():
    def __init__(self):
        self.modelo = Modelo()
    
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