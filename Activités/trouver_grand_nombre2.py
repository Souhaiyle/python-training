liste = [1,2,3,5,6,7]
def nb_max():
    maximum = 0
    for i in liste:
        if i > maximum:
            maximum = i
    print("Le plus grand nombre est",maximum)
    print("Le rang de ce nombre est",liste.index(maximum))

nb_max()

