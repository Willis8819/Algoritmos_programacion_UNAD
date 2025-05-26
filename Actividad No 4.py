"""
La empresa Netflix desea saber cuál es el género favorito de streaming entre 5 personas. 
Para esto, le ha solicitado su ayuda para desarrollar un programa para saber cuál es el género con más votos entre: 
acción y ciencia ficción. El programa debe capturar la preferencia de las 5 personas y mostrar cuál de los géneros es el favorito.
"""

voto1=input("Ingrese cual es su genero favorito (accion o ciencia ficcion): ")
voto2=input("Ingrese cual es su genero favorito (acción o ciencia ficcion): ")
voto3=input("Ingrese cual es su genero favorito (acción o ciencia ficcion): ")
voto4=input("Ingrese cual es su genero favorito (acción o ciencia ficcion): ")
voto5=input("Ingrese cual es su genero favorito (acción o ciencia ficcion): ")

if voto1 == "accion":
    if voto2 == "accion":
        if voto3 == "accion":
            if voto4 == "accion":
                if voto5 == "accion":
                    print("El género favorito es: Acción")
                else:
                    print("El género favorito es: Acción")
            else:
                if voto5 == "accion":
                    print("El género favorito es: Acción")
                else:
                    if voto4 == "ciencia ficcion" and voto5 == "ciencia ficcion":
                        print("El género favorito es: Acción")
                    else:
                        print("Empate")
        else:
            if voto4 == "accion" and voto5 == "accion":
                print("El género favorito es: Acción")
            else:
                if voto3 == "ciencia ficcion" and voto4 == "ciencia ficcion" and voto5 == "ciencia ficcion":
                    print("El género favorito es: Ciencia Ficción")
                else:
                    print("Empate")
    else:
        print("Empate o género favorito depende de combinaciones específicas")
else:
    if voto1 == "ciencia ficcion":
        if voto2 == "ciencia ficcion":
            if voto3 == "ciencia ficcion":
                if voto4 == "ciencia ficcion":
                    if voto5 == "ciencia ficcion":
                        print("El género favorito es: Ciencia Ficción")
                    else:
                        print("El género favorito es: Ciencia Ficción")
                else:
                    if voto5 == "ciencia ficcion":
                        print("El género favorito es: Ciencia Ficción")
                    else:
                        print("Empate")
            else:
                print("Empate o género favorito depende de combinaciones específicas")
        else:
            print("Empate o género favorito depende de combinaciones específicas")
    else:
        print("Empate o datos inválidos")