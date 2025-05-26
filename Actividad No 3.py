"""
El almacén “viste con estilo” requiere de su ayuda para construir un programa que permita calcular la talla de ropa acorde 
a la altura ingresada así (la altura debe capturarse en centímetros):


       ALTURA                        TALLA 
MENOR O IGUAL A 150                    S
MAYOR A 150 Y MENOR A 170              M 
MAYOR O IGUAL A 170 Y MENOR A 180      L
MAYOR O IGUAL A 180                    XL
"""

altura=float(input("Ingrese la altura en centimetros: "))
if altura <= 150:
    print("Su talla es: S")
elif altura < 170:
    print("Su talla es: M")
elif altura < 180:
    print("Su talla es: L")
else:
    print("Su talla es: XL")