class Modelo():
    def __init__(self, texto):
        self.texto = texto
    
class Vista():
    def __init__(self):
        self.modelo = Modelo()
    
    def imprimir(self):
        print(self.modelo.texto)