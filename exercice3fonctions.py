count_alpha = len("Hello world!")
print("Le nombre de caractères dans la chaîne est :", count_alpha)
count_float = float(count_alpha)
print("Le nombre de caractères converti en float est :", count_float)



import math
round_pi = round(math.pi, 2)



reversed_text = list("Hello world!"[::-1])
print("Texte inversé :", reversed_text)



age = input("Veuillez saisir votre âge : ")
print("Vous avez {} ans.".format(age))
print("Le type de la variable age est :", type(age))



num =[2,8,1,4,6,3,7]
sorted_num = sorted(num)
print("Nombres triés :", sorted_num)
sum_of_list = sum(num)
print("Somme des nombres dans la liste :", sum_of_list)
min_value = min(num)
print("Valeur minimale dans la liste :", min_value)
max_value = max(num)
print("Valeur maximale dans la liste :", max_value)

calc = "1 + 2"
string_interpret = eval(calc)
print("Résultat de l'évaluation de l'expression :", string_interpret)

