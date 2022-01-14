texte = input("Entrez une phrase:")
lettre = input("Entrez un lettre:")
liste = []
for i in range(len(texte)):
    if texte[i] == lettre:
        liste.append(i)
print("il y a",len(liste),"fois la lettre",lettre)
print("la position de la lettre est",liste)
