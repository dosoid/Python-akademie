"""
projekt_1.py: první projekt do Engeto Online Python Akademie

author: Evžen Oskin
email: dos333@seznam.cz
"""

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

# Seznam uživatelů

uzivatele = {"bob": "123", "ann": "pass123", "mike": "password123", "liz": "pass123"}

# Uživatel zadá své jméno a heslo

jmeno = input("Zadej své uživatelské jméno: ")
heslo = input("Zadej své heslo: ")

# Proměnné pro práci s textem

pocet_text = len(TEXTS) # počet textů v slovníku TEXTS
pocet_slov = 0
pocet_slov_velke_pismeno = 0
pocet_slov_vse_velke = 0
pocet_slov_vse_male = 0
pocet_cisel = 0
soucet_cisel = 0
slovnik_delka_slov = dict()

# Ověření uživatele

if uzivatele.get(jmeno) == heslo:
    print(f"Vítej v aplikaci, {jmeno}!", "_" * 30, sep="\n")
else:
    print("Zadané jméno nebo heslo není správné. Ukončuji program.")
    exit()

# Uživatel vybere text

vybrany_text_cislo = input(f"Vyber si text zadáním čísla 1 - {pocet_text}: ")
if vybrany_text_cislo.isdecimal():
    if 0 < int(vybrany_text_cislo) < (pocet_text + 1):
        print(f"Vybral jsi text číslo {vybrany_text_cislo}", "_" * 30, sep="\n")
        text_cislo = int(vybrany_text_cislo) - 1
    else:
        print("Zadal jsi číslo mimo rozsah. Ukončuji program.")
        exit()
else:
    print(f"Nezadal jsi číslo v rozmezi 1 - {pocet_text}. Ukončuji program.")
    exit()

# Projde se text a provede výpočty

for slovo in TEXTS[text_cislo].split():
    slovo = slovo.strip(",.;")
    pocet_slov += 1   
    # Délka slova a přiřazení do slovníku podle délky
    delka_slova = len(slovo)
    slovnik_delka_slov[delka_slova] = slovnik_delka_slov.get(delka_slova, 0) + 1
    # Podmínky pro výpočty
    if slovo.isnumeric():
        pocet_cisel += 1
        soucet_cisel += int(slovo)
    elif slovo.isalpha():
        if slovo.istitle() or slovo.isupper():
            pocet_slov_velke_pismeno += 1
        if slovo.isupper():
            pocet_slov_vse_velke += 1
        if slovo.islower():
            pocet_slov_vse_male += 1
    #print(slovo)

# Vypíše jednotlivé proměnné

print(f"Počet slov v textu: {pocet_slov}",
      f"Počet slov začínajících velkým písmenem: {pocet_slov_velke_pismeno}",
      f"Počet slov psaných velkými písmeny: {pocet_slov_vse_velke}",
      f"Počet slov psaných malými písmeny: {pocet_slov_vse_male}",
      f"Počet čísel v textu: {pocet_cisel}",
      f"Součet všech čísel: {soucet_cisel}",
      "_" * 20,
      sep="\n"
      )

# Maximální délka slova v slovníku

max_delka = max(slovnik_delka_slov.values())

# Připraví hlavičku tabulky

print(
    "{:>5}".format("Délka"),
    "|{0:^{1}}|".format("Opakování", max_delka),
    "{:<5}".format("Počet")
)   

# Seřadí tabulku a vypíše

serazena_tabulka = dict(sorted(slovnik_delka_slov.items()))
for key in serazena_tabulka.keys():
    print(
        "{:>5}".format(key),
        "|{0:<{1}}|".format(slovnik_delka_slov[key] * "*", max_delka),
        "{:<5}".format(slovnik_delka_slov[key])
    )
   
