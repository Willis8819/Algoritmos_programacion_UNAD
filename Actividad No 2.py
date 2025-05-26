"""
Construir un programa que permita verificar si una persona es mayor de edad. Para esto debe solicitar el año de nacimiento,
calcular la edad y si la edad es mayor o igual a 18 mostrar un mensaje por consola que indique que la persona es mayor de edad,
de lo contrario que muestre un mensaje indicando que es menor de edad.
"""

anio_nacimiento=int(input("Ingrese año de nacimiento: "))
anio_actual=int(input("Ingrese año actual: "))
edad=anio_actual-anio_nacimiento
if edad>=18:
    print("La persona es mayor de edad")
else:
    print("Es menor de edad")

