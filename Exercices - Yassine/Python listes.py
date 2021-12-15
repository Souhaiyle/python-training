# Montrer quel est le plus grand nombre et montrer son rang (1,2,3,4...)

liste = [14, 5 , 8, 12, 3, 76, 2, 15, 6]
def recherche_max():
    maximum = 0
    for n in liste:
        if n > maximum:
            maximum = n
    print(maximum)
    print(liste.index(maximum))

recherche_max()


