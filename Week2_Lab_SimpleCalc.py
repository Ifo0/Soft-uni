# P = a + b + a + b
# S = a.b

#Zadacha 1
# x1 = float(input())
# y1 = float(input())
# x2 = float(input())
# y2 = float(input())
#
#
# strana_a = abs(x1 - x2)
# strana_b = abs(y2 - y1)
#
# lice = strana_a * strana_b
# perimetur = 2 * (strana_a + strana_b)
#
# print(lice)
# print(perimetur)


# #Zadacha 2
#
# # 1 USD = 1.79549 BGN.
#
# dollars = float(input())
# lev = dollars * 1.79549
#
# print(f"{lev:.2f}")
# import math
# print(f'The value of pi is approximately {math.pi:.3f}.')

#Zadacha 3


# stoinost = float(input())
# vhodna_valuta = input()
# izhodna_valuta = input()
#
# kursove = {"USD": 1.79549,"EUR": 1.95583 , "GBP": 2.53405, "BGN": 1}
#
# convertirana_valuta = stoinost * (kursove[vhodna_valuta] / kursove[izhodna_valuta])
#
# print(f"{convertirana_valuta:.2f}")


# Zadacha 4

# broi_masi = int(input())
# dulzina_masi = float(input())
# shirochina_masi = float(input())
#
# cena_kvadrat_pokrivka = 7
# cena_kvadrat_kare = 9
# kurs_bgn = 1.85
#
# plosht_pokrivki = broi_masi * ((dulzina_masi + 2 * 0.30) * (shirochina_masi + 2 * 0.30))
# plosht_kareta = broi_masi * ((dulzina_masi / 2) * (dulzina_masi / 2))
#
# cena_pokrivki = plosht_pokrivki * cena_kvadrat_pokrivka
# cena_kareta = plosht_kareta * cena_kvadrat_kare
# obshta_cena = cena_pokrivki + cena_kareta
# print(f'{obshta_cena:.2f} USD')
# print(f'{obshta_cena * kurs_bgn:.2f} BGN')

#Zadacha 5
# import math
#
# duljina_m = float(input())
# shirina_m = float(input())
# strana_garderob_m = float(input())
#
# zala = (duljina_m * 100) * (shirina_m * 100)
# garderob = (strana_garderob_m * 100) * (strana_garderob_m * 100)
#
# peika = zala / 10
# svobodo_prostranstova = zala - garderob - peika
# broi_tanciori = svobodo_prostranstova // (40 + 7000)
# print(int(broi_tanciori))


# Zadacha 6


# dni_kampania = int(input())
# sladkari_broi = int(input())
# torti_broi = float(input()) * 45
# gofreti = float(input()) * 5.80
# palachinki = float(input()) * 3.20
#
# suma_kampania = ((torti_broi + gofreti + palachinki) * sladkari_broi) * dni_kampania
# suma_kraina = suma_kampania - ((1/8) * suma_kampania)
# print(f'{suma_kraina:.2f}')


#Zadacha 7
whiskey_price = float(input())
bear = float(input())
wine = float(input())
rakja = float(input())
whiskey = float(input())

price_rakja = whiskey_price / 2
price_bear = 0.2 * price_rakja
price_wine = 0.6 * price_rakja

total_sum = (whiskey_price * whiskey) + (bear * price_bear) + (price_rakja * rakja) + (price_wine * wine)

print(f'{total_sum:.2f}')












