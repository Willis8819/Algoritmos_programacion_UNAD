"""
La escuela ECAPMA de la UNAD está desarrollando un estudio para verificar el cambio climático en su ciudad. 
Para esto, le ha pedido su ayuda en la construcción de un programa que solicite las temperaturas de los últimos 5 días 
y muestre el promedio de temperaturas si el promedio es mayor o igual a 22 grados, debe informar que el clima es cálido 
si es menor que es frio.
"""
temp_1=float(input("Ingrese la temperatura No 1: "))
temp_2=float(input("Ingrese la temperatura No 2: "))
temp_3=float(input("Ingrese la temperatura No 3: "))
temp_4=float(input("Ingrese la temperatura No 4: "))
temp_5=float(input("Ingrese la temperatura No 5: "))
promedio=(temp_1+temp_2+temp_3+temp_4+temp_5)/5
if promedio>=22:
    print("El clima es cálido")
else:
    print("El clima es frio")