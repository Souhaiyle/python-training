#ecrire un programme pour qui affiche la somme des entiers de 1 à 10 c'est à dire 1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 + 10.
#aide : utiliser une boucle

#methode 1
s = 0
for i in range(1,11):
    s = i + s
print(s)

#creation d'une fonction
def somme_entiers(b):
    s = 0
    for i in range(1,b+1):
        s = i + s
    print(s)


somme_entiers(2)

