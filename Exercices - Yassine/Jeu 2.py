from random import *
nombre_machine = randint(0, 100)

def devinne_mon_nombre():
    print("Vous avez 5 essais maximum pour trouver le nombre")
    compteur = 5
    while(0,100):
        compteur = compteur -1
        if compteur == -1:
            print("Perdu, vous n'avez plus d'essais. Il faut recommencer")
            break
        nombre_utilisateur = int(input("Entrer un nombre :"))
        if nombre_utilisateur > nombre_machine:
            print("Moins")
            print("Il vous reste",compteur,"essais")
        elif nombre_utilisateur == nombre_machine:
            print("Bravo, vous avez trouver le nombre")
            break
        else:
            print("Plus")
            print("Il vous reste", compteur, "essais")


devinne_mon_nombre()










