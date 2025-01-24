# ukol1
# prvni_cislo = 5
# druhe_cislo = 5
# def vynasob(num1, num2):
#     return num1 * num2
# vysledek = vynasob(prvni_cislo, druhe_cislo)
# print(vysledek)

#ukol2
# vstup = 'Ahoj všem'
# def zdvojnasob_vsechny_znaky(zadani):
#     seznam = []
#     for znak in zadani:
#         seznam.append(znak * 2)
#     return "".join(seznam)

# vysledek = zdvojnasob_vsechny_znaky(vstup)
# print(vysledek)

# #ukol3
# import sys
# def je_os_windows():
#     return True if sys.platform.startswith('win') else False

# print(je_os_windows())
# print(sys.platform)

#ukol4

# def najdi_gcd(x1: int, x2: int) -> int:
#     '''Vrati nejvetsi spolecny delitel dvou cisel'''
#     while x2 > 1:
#         zbytek_po_deleni = x1 % x2
#         if zbytek_po_deleni == 0:
#             break
#         x1, x2 = x2, zbytek_po_deleni
#     return x2
# vysledek = najdi_gcd(20, 16)
# print(vysledek)