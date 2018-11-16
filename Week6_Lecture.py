# Zadacha 1:

# for i in range(1, 101):
#     print(i)

# Zadacha 2:
# for i in range(ord('a'), ord('z') + 1):
#     print(chr(i))

# Zadacha 3
# n = int(input())
# zumme = 0
#
# for i in range(n):
#     get = int(input())
#     zumme += get
#
# print(zumme)

# Zadacha 4
## import sys; sys.maxsize or -sys.minsize - 1
# n = int(input())
# max = None
# bootstrap = 0
#
# for i in range(n):
#     get = int(input())
#     if bootstrap == 0:
#         max = get
#         bootstrap += 1
#     if get > max:
#         max = get
#
# print(max)

# Zadacha 5
# n = int(input())
# min = None
# get = int(input())
# min = get
#
# for i in range(n - 1):
#     get = int(input())
#     if get < min:
#         min = get
#
# print(min)

# Zadacha 6
# n = int(input()) * 2
# left_sum = 0
# right_sum = 0
#
# for i in range(n):
#     if i < n / 2:
#         left_get = int(input())
#         left_sum += left_get
#     else:
#         right_get = int(input())
#         right_sum += right_get
#
# if left_sum == right_sum:
#     print(f'Yes, sum = {right_sum}')
# else:
#     print(f'No, diff = {abs(left_sum - right_sum)}')

# Zadacha 7
# n = int(input())
# even_sum = 0
# odd_sum = 0
#
# for i in range(n):
#     get = int(input())
#     if i % 2 == 0:
#         even_sum += get
#     else:
#         odd_sum += get
#
# if even_sum == odd_sum:
#     print(f'Yes')
#     print(f'Sum = {even_sum}')
# else:
#     print(f'No')
#     print(f'Diff = {abs(even_sum - odd_sum)}')

# Zadacha 8
# vowels = ['a', 'e', 'i', 'o', 'u']
# a = 1
# e = 2
# i = 3
# o = 4
# u = 5
#
# word = input()
# sum = 0
#
# for letter in word:
#     if letter in vowels:
#         sum += eval(letter)
#
# print(sum)

# Zadacha 9
# age = int(input())
# washing_machine = float(input())
# price_per_toy = float(input())
# money_gift = 10
# total_money = 0
# number_of_toys = 0
#
# for birthday in range(1, age + 1):
#     if birthday % 2 == 0:
#         total_money += money_gift - 1 #because her bro takes 1 every time
#         money_gift += 10
#     else:
#         number_of_toys += 1
#
# sold_toys_sum = number_of_toys * price_per_toy
# total_save = total_money + sold_toys_sum
#
# if total_save >= washing_machine:
#     print(f'Yes! {total_save - washing_machine:.2f}')
# else:
#     print(f'No! {washing_machine - total_save:.2f}')