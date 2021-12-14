from random import *
nombre_machine = randint(0, 100)
def devinne_mon_nombre():
    print("Vous avez 5 essais maximum pour trouver le nombre")
    nombre_utilisateur = -1 #on lui donne une valeur au hasard pour rentrer dans le while
    nombre_essais = 5
    while nombre_machine != nombre_utilisateur :
        nombre_essais = nombre_essais - 1
        if nombre_essais == -1 : #on verifie d'abord si il reste des essais pour l'utilisateur
            print("Vous n'avez plus d'essais ! Mon chifre était : ",nombre_machine)
            break
        else : #si c'est bien le cas alors on lance le process
            #début des boucles imbriquées
            nombre_utilisateur = int(input("Entrer un nombre :")) #on redemande le nombre à l'utilisateur
            #début des comparaison
            if nombre_utilisateur > nombre_machine:
                print("Raté, c'est moins ! Il vous reste",nombre_essais,"essai(s)")
            elif nombre_utilisateur < nombre_machine:
                print("Toujours pas, c'est plus ! Il vous reste",nombre_essais,"essai(s)")
            else :
                print("Bonne réponse ! Bravo")









devinne_mon_nombre()










