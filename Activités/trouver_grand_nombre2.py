liste = [1,2,3,5,6,7]
def nb_max():
    maximum = 0
    for i in liste:
        if i > maximum:
            maximum = i
    print(maximum)
    print(liste.index(maximum))


nb_max()

