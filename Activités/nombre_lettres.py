texte = input("Entrer une phrase:")
lettre = input("Entrer une lettre:")
rangs = []
for i in range(len(texte)):
    if texte[i] == lettre:
        rangs.append(i)
print("il y a",len(rangs),"la lettre",lettre)
print("La position de la lettres est ",rangs)