def number(nb):
    nb = int(input("Entrez un nombre :"))
    if nb < 10 :
        print("Le nombre est pas compris entre 10 et 100")
    elif nb > 100:
        print("Le nombre est pas compris entre 10 et 100")
    else:
        print("Le nombre est compris entre 10 et 100")

    nb = nb%2
    if nb == 0:
        print("Le nombre est pair")
    elif nb == 1:
        print("Le nombre est impair")

    if nb == 0 :
        print(bin(nb))
    elif nb == 1:
        print(hex(nb))

number(100)




