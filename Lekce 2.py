# Úkol 2.1

# zamestnanci = [
#     'František', 'Bruno',
#     'Anna', 'Jakub',
#     'Klára', 'Anežka',
#     'Anežka', 'Anežka'
# ]

# posledni_index = len(zamestnanci) - 1

# print(f"Na indexu 2 je: {zamestnanci[2]}")
# print(f"Na {posledni_index} indexu je: {zamestnanci[posledni_index]}")
# print(f"V intervalu od 2 do 5 je: {zamestnanci[2:6]}")
# print(f"Každý 3.člen je: {zamestnanci[::3]}")

# Úkol 2.2

# jmeno = "Martin"
# vaha = 80
# vyska = 2
# bmi = vaha / (vyska**2)
# kategorie = ""
# if bmi < 18.5:
#     kategorie = "Podvýživa"
# elif bmi <= 25:
#     kategorie = "Zdravá váha"
# elif bmi <= 30:
#     kategorie = "Mírná nadváha"
# elif bmi <=40:
#     kategorie = "Obezita"
# else:
#     kategorie = "Těžká obezita"

# print(f"{jmeno} tvé BMI je {bmi}, což spadá do kategorie {kategorie}")

# Úkol 2.3

# zamestnanci = ['František','Anna','Jakub','Klára']
# print(f"Zaměstnanci na začátku: {zamestnanci}")
# zamestnanci_a = zamestnanci.copy()
# zamestnanci_a.extend(['Bruno','Anežka'])
# print(f"Nová jména: {zamestnanci_a}")
# zamestnanci_b = zamestnanci.copy()
# zamestnanci_b.insert(1,'Bruno')
# print(f"Nová jména vložena: {zamestnanci_b}")

# úKOL 2.4

# vstupni_cisla = [1, 2, 3, 4, 5, 6, 7]
# vstupni_pismena = ["p", "ú", "s", "č", "p", "s", "n"]
# tyden = ('pondělí', 'úterý', 'středa', 'čtvrtek', 'pátek', 'sobota', 'neděle')
# cislo_dne = 3
# if cislo_dne in vstupni_cisla:
#     print("Správná vstupní hodnota!")
#     den_tydne = tyden[cislo_dne-1]
#     if den_tydne.startswith(vstupni_pismena[cislo_dne-1]):
#         print("Správné písmeno")
#     else:
#         print("Špatné písmeno")
# else:
#     print("Špatná vstupní hodnota")
