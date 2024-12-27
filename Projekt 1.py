"""
projekt_1.py: první projekt do Engeto Online Python Akademie

author: Evžen Oskin
email: evzen.osk@gmail.com
"""
'''
author =
'''
TEXTS = ['''
Situated about 10 miles west of Kemmerer,
Fossil Butte is a ruggedly impressive
topographic feature that rises sharply
some 1000 feet above Twin Creek Valley
to an elevation of more than 7500 feet
above sea level. The butte is located just
north of US 30N and the Union Pacific Railroad,
which traverse the valley. ''',
'''At the base of Fossil Butte are the bright
red, purple, yellow and gray beds of the Wasatch
Formation. Eroded portions of these horizontal
beds slope gradually upward from the valley floor
and steepen abruptly. Overlying them and extending
to the top of the butte are the much steeper
buff-to-white beds of the Green River Formation,
which are about 300 feet thick.''',
'''The monument contains 8198 acres and protects
a portion of the largest deposit of freshwater fish
fossils in the world. The richest fossil fish deposits
are found in multiple limestone layers, which lie some
100 feet below the top of the butte. The fossils
represent several varieties of perch, as well as
other freshwater genera and herring similar to those
in modern oceans. Other fish such as paddlefish,
garpike and stingray are also present.'''
]
# Uživatel zadá své jméno a heslo
jmeno = input("Zadej své uživatelské jméno: ")
heslo = input("Zadej své heslo: ")
# Seznam uživatelů
uzivatele = {bob: "123", ann: "pass123", mike: "password123", liz: "pass123"}
# Proměnné pro práci s textem
text_cislo = int()
pocet_slov = int()
pocet_slov_velke_pismeno = int()
pocet_slov_vse_velke = int()
pocet_slov_vse_male = int()
pocet_cisel = int()
soucet_cisel = int()

if uzivatele.get(jmeno) == heslo:
    print(f"Vítej v aplikaci, {jmeno}!")
else:
    print("Zadané jméno nebo heslo není správné. Ukončuji program.")
    exit()

vybrany_text_cislo = input("Vyber si text zadáním čísla 1 - 3: ")
if vybrany_text_cislo.isnumeric():
    if 0 < int(vybrany_text_cislo) < 4:
        print(f"Vybral jsi text číslo {vybrany_text_cislo}.")
        text_cislo = int(vybrany_text_cislo) - 1
    else:
        print("Zadal jsi číslo mimo rozsah 1 - 3. Ukončuji program.")
        exit()
else:
    print("Nezadal jsi číslo v rozmezi 1 - 3. Ukončuji program.")
    exit()




