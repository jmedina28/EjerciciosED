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
        while self.condicionn <= 10:
            Mostrar(self.bloque).mostrar()
            self.condicionn += 1


class Mostrar:
    # Una instrucción para mostrar un mensaje
    # en salida estándar.
    def __init__(self, mensaje):
        self.mensaje = mensaje

    def mostrar(self):
        print(self.mensaje)

def visitante():
    mostrar_ok = "OK"
    mostrar_ko = "KO"
    alternativa = Si(2 + 2 == 4, mostrar_ok, mostrar_ko)
    alternativa.ejecutar()
