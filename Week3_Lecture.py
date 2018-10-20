#Started watching one hour into the lecture

#LAB

#Zadacha 1
# ocenka = float(input())
#
# if ocenka >= 5.50:
#     print("Excellent!")
#
# #Zadacha 2

# chislo = int(input())
#
# if chislo % 2 == 0:
#     print('even')
# else:
#     print('odd')

#Zadacha 3
# a = int(input())
# b = int(input())
#
# if a > b:
#     print(a)
# else:
#     print(b)


#Zadacha 4
# chislo = int(input())
#
# if chislo >= 10:
#     print('number too big')
# elif chislo == 1:
#     print('one')
# elif chislo == 2:
#     print('two')
# elif chislo == 3:
#     print('three')
# elif chislo == 4:
#     print('four')
# elif chislo == 5:
#     print('five')
# elif chislo == 6:
#     print('six')
# elif chislo == 7:
#     print('seven')
# elif chislo == 8:
#     print('eight')
# elif chislo == 9:
#     print('nine')
# else:
#     print('')

#Zadacha 5
# password = input()
#
# if password == 's3cr3t!P@ssw0rd':
#     print("Welcome")
# else:
#     print("Wrong password!")

#Zadacha 6
# input = int(input())
#
# if input < 100:
#     print('Less than 100')
# elif input >= 100 and input <= 200:
#     print('Between 100 and 200')
# else:
#     print('Greater than 200')

#Zadacha 7
# duma_1 = input()
# duma_2 = input()
#
# if duma_1.lower() == duma_2.lower():
#     print('yes')
# else:
#     print('no')

#Zadacha 8
# import math
# figura = input()
# area = None
#
# if figura == 'square':
#     a = float(input())
#     print(f'{a*a:.3f}'.rstrip('0').rstrip('.'))
# elif figura == 'rectangle':
#     a = float(input())
#     b = float(input())
#     print(f'{a*b:.3f}'.rstrip('0').rstrip('.'))
# elif figura == 'circle':
#     r = float(input())
#     print(f'{math.pi*(r**2):.3f}'.rstrip('0').rstrip('.'))
# elif figura == 'triangle':
#     a = float(input())
#     h = float(input())
#     print(f'{(a*h)/2:.3f}'.rstrip('0').rstrip('.'))
#
# print(area) Ako imah tozi var, vmesto da go pisha pod vseki if else, direktno
# Neobhodimo da se suzdava (definira) predvaritelno inache shte bude premahnata ot garbige collector-a

#Zadacha 9
# a = int(input())
# b = int(input())
# c = int(input())
#
# if a == b == c:
#     print('yes')
# else:
#     print('no')

#Zadacha 10

vacation_cost = float(input())
puzzles = int(input())
dolls = int(input())
bears = int(input())
minions = int(input())
trucks = int(input())

sum = puzzles * 2.60 + dolls * 3 + bears * 4.10 + minions * 8.20 + trucks * 2
number_toys = puzzles + dolls + bears + minions + trucks

if number_toys >= 50:
    sum = (1 - 0.25) * sum  #sum - sum * 0.25

rent = 0.1 * sum
profit = sum - rent

if profit >= vacation_cost:
    diff = profit - vacation_cost
    print(f'Yes! {diff:.2f} lv left.')
else:
    diff = vacation_cost - profit
    print(f'Not enough money! {diff:.2f} lv needed.')

#Notes
#Garbigge collection and life of the variable

# input = int(input())
# num_1 = 1
#
# if input == 1:
#     num_1 = 2
#     print(num_1)
#
# print(num_1)
#
# a = input()
# b = len(a)
# print(b)