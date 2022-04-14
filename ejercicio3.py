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
class Naturaleza():
    def __init__(self, naturaleza):
        self.naturaleza = naturaleza
    def ALIMENTARIA(self):
        self.naturaleza = "ALIMENTARIA"
    def SERVICIO(self):
        self.naturaleza = "SERVICIO"
class Producto(Naturaleza):
    def __init__(self, naturaleza):
        self.naturaleza = Naturaleza(naturaleza)
        self.precio_bruto = 100


class FactoryFactura():
    def crear():
        producto = Producto(input("Introduzca la naturaleza del producto: "))
    
    def facturar():
        if producto.naturaleza == "ALIMENTARIA":
            precio_neto = producto.precio_bruto * 1.055
        elif producto.naturaleza == "SERVICIO":
            precio_neto = producto.precio_bruto * 1.2
producto = Producto(Naturaleza.SERVICIO)
precio_neto = FactoryFactura.crear().facturar() 
print(precio_neto) 
    