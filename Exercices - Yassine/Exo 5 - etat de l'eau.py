#Ecrire un programme qui prend en entrée une température t et qui renvoie l'état de l'eau à cette température c'est à dire "SOLIDE", "LIQUIDE" ou "GAZEUX".

#On prendra comme conditions les suivantes :

#Si la température est strictement négative alors l'eau est à l'état solide.
#Si la température est entre 0 et 100 (compris) l'eau est à l'état liquide.
#Si la température est strictement supérieure à 100.

def temp(t):
    t <= 0 and t >= 101
    if t < 0:
        print("L'état de l'eau est Solide")

    elif t > 100:
        print("L'état de l'eau est Gazeux")

    else:
        print("L'état de l'eau est Liquide")



temp(50)

