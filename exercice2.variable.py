age = 32
age += 10
divage = age // 7
print(divage)
restdiv = divage ** 3
print(restdiv)
expdiv = 3 ** 3
print(expdiv)

nombre = int(input("Saisir un nombre entier: "))
type_nombre = type(nombre)
print(nombre) 
print(type_nombre)

prix_lait = 0.45
prix_cidre = 3.85
prix_farine = 0.90
prix_beurre = 0.77
prix_nutella = 1.87

2 * prix_lait
3 * prix_cidre
1 * prix_farine
1 * prix_beurre
1 * prix_nutella

orderPrice = 2 * prix_lait + 3 * prix_cidre + 1 * prix_farine + 1 * prix_beurre + 1 * prix_nutella
print(orderPrice)

allowageMoney = 20

reste = allowageMoney - orderPrice
print(reste)


if reste > 0:
    message = ("Il vous reste {} €".format(reste))
elif reste < 0:
    message = ("Vous devez payer {} € de plus".format(abs(reste))) 
else:
    message = "Vous n'avez plus d'argent"
print(message)

