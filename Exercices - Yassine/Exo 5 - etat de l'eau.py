#Ecrire un programme qui prend en entrée une température t et qui renvoie l'état de l'eau à cette température c'est à dire "SOLIDE", "LIQUIDE" ou "GAZEUX".

#On prendra comme conditions les suivantes :

#Si la température est strictement négative alors l'eau est à l'état solide.
#Si la température est entre 0 et 100 (compris) l'eau est à l'état liquide.
#Si la température est strictement supérieure à 100.


def temperature(t):
    if t < 0:
        print("L'eau est à l'état solide")
    elif t >= 0 & t <= 100:
        print("L'eau est à l'état liquide")
    else :
        print("L'eau est à l'état gazeux")

def temperature2(t):
    if t > 100:
        print("L'eau est à l'état gazeux")
    elif t >= 0 & t <= 100:
        print("L'eau est à l'état liquide")
    else :
        print("L'eau est à l'état solide")


temperature2(500)

