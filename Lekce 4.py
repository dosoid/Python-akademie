# Ukol 1
# veta = 'Zvuk řeči je produkován poměrně otevřenou konfigurací vokálního traktu'
# samohlasky = 'aeiouáéíóú'
# souhlasky = 'bcčdďfghjklmnňprřsštťvzžcdž'
# vysledek = dict()
# pocet_samohlasky = int()
# pocet_souhlasky = int()

# for pismeno in veta:
#     if pismeno.lower() in samohlasky:
#         pocet_samohlasky += 1
#     elif pismeno.lower() in souhlasky:
#         pocet_souhlasky += 1

# vysledek[samohlasky] = pocet_samohlasky
# vysledek[souhlasky] = pocet_souhlasky

# print(f"Počet souhlasek: {vysledek[souhlasky]} | Počet samohlasek: {vysledek[samohlasky]}")

# Ukol 2 

# cisla = [1, 2, 3, 4, 5, 6, 7, 8]
# suda = 0
# licha = 0
# for cislo in cisla:
#     if cislo % 2 == 0:
#         suda += cislo
#     else:
#         licha += cislo
# vysledek = abs(suda - licha)
# print(f"Rozdíl je: {vysledek}")

# Ukol 3

# vysledek = list()
# start = 3
# stop = 9
# delitel = 3

# if isinstance(start, int) and isinstance(stop, int) and isinstance(delitel, int):
#     for cislo in range(start,stop+1):
#         if cislo % int(delitel) == 0:
#             vysledek.append(cislo)
#     print(f"Zadaný rozsáh: <{start}, {stop}> \n", 
#           f"Čísla dělitelná 3: {vysledek}")
# else:
#     print(f"Zadaný rozsáh: <{start}, {stop}>, dělitel: {delitel} \n", "Zadané vstupy musí být čísla.")    

# Ukol 4

seznam_slov = ["jablko", "pomeranč", "banán", "kiwi", "hruška"]
delky_slov = {slovo: len(slovo) for slovo in seznam_slov}
print(delky_slov)
