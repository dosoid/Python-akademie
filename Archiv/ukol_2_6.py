# ukol 2_6
# hra kamen nůžky papír
# import random

# moznosti = ["kamen", "nuzky", "papir"]
# hrac = "kamen"
# pocitac = random.choice(moznosti)

# print("Hráč:" , hrac)
# print("Počítač: ", pocitac)

# if hrac == "kamen" and pocitac == "nuzky":
#     print("Hráč vyhrál")
# elif hrac == "kamen" and pocitac == "papir":
#     print("Počítač vyhrál")
# else:
#     print("Nerozhodně")

# ukol vytvoř složky
# import os

# jmena_slozek = ["obrazky", "texty", "gify"]
# print(os.getcwd())
# for jmeno in jmena_slozek:
#     if jmeno not in os.listdir():
#         os.mkdir(jmeno)
#         print(f"Tvořím novou složku: {jmeno}")
#     else:
#         print(f"Složka {jmeno} již existuje.")

# print("Všechny složky existují.")

# ukol Hod kostkou
# import random

# min_hodnota = 1
# max_hodnota = 6
# while True:
#     print("Házím kostkou..")
#     hod = random.randint(min_hodnota, max_hodnota)
#     print(f"Na kostce je {hod}")
#     if hod != 6:
#         print("Konec hry")
#         break

