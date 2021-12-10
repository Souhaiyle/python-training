def number(nb):
    nb = int(input("Entrez un nombre :"))
    if nb < 10 :
        print("Le nombre est pas compris entre 10 et 100")
    elif nb > 100:
        print("Le nombre est pas compris entre 10 et 100")
    else:
        print("Le nombre est compris entre 10 et 100")

    pair_impair = nb%2
    if pair_impair == 0:
        print("Le nombre est pair", "donc binaire est : ",bin(nb))
    elif pair_impair == 1:
        print("Le nombre est impair", "donc héxa est :" , hex(nb))

number(10000)
