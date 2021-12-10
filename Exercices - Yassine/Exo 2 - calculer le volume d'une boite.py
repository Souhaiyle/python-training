# 2 : créer une fonction volume_boite() qui prend en parametre la longueur l la largeur larg et la hauteur h
# Puis determiner le volume d'une boite à partir des variables suivantes

#ici on crée un foction volume_boite() et on determine le volume grace au variables l, h, L

#creation de la fonction

def volume_boite(l,h,L):
    volume = l*h/L
    print("volume = ",volume)


# Test de la fonction
volume_boite(4, 8, 2)

# question : air d'un triangle A = 1/2b x h
def air_triangle(b,h):
    air = (b*h)/2
    print("L'air du triangle est de ",air, "cm²")


air_triangle(4,6)









