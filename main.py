

def seleccionejercicio(variable):
    if variable == 1:
        from ejercicio1 import visitante
        visitante(int(input("Si desea ejecutar el ejemplo del enunciado pulse 1, en cambio si desea probar el bucle de la clase MientrasQue pulse 2: ")))
    elif variable == 2:
        from ejercicio2 import Cliente
        Cliente()
    elif variable == 3:
        import ejercicio3

    else:
        print("Introduzca valores correctos por favor.")
        seleccionejercicio(int(input("""
1 - Visitante.
2 - MVC Mayúsculas.
3 - IVA.

Seleccione que ejercicio desea ejecutar(1-3): """)))


variable = int(input("""
1 - Visitante.
2 - MVC Mayúsculas.
3 - IVA.

Seleccione que ejercicio desea ejecutar(1-3): """))

if __name__ == "__main__":
    seleccionejercicio(variable)