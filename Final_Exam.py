# Zadacha 1

# group_size = int(input())
# carabins = int(input())
# ropes = int(input())
# pikels = int(input())
# dds = 1.2
#
# to_pay = group_size * (carabins * 36 + ropes * 3.60 + pikels * 19.80) * 1.2
# print(f'{to_pay:.2f}')

# Zadacha 2
# import math
# absence_days = int(input())
# food_in_kg = int(input())
# first_dog_rations_day = float(input())
# second_dog_rations_day = float(input())
# third_dog_rations_day = float(input())
#
# food_consumed = absence_days * (first_dog_rations_day + second_dog_rations_day + third_dog_rations_day)
#
# if food_consumed <= food_in_kg:
#     print(f'{math.floor(food_in_kg - food_consumed)} kilos of food left.')
# else:
#     print(f'{math.ceil(food_consumed - food_in_kg)} more kilos of food are needed.')

# Zadacha 3

# fruit = input()
# size = input()
# order_size = int(input())
# to_pay = 0
#
# if fruit == 'Watermelon':
#     if size == 'small':
#         to_pay = 56 * 2 * order_size
#     elif size == 'big':
#         to_pay = 28.70 * 5 * order_size
# elif fruit == 'Mango':
#     if size == 'small':
#         to_pay = 36.66 * 2 * order_size
#     elif size == 'big':
#         to_pay = 19.60 * 5 * order_size
# elif fruit == 'Pineapple':
#     if size == 'small':
#         to_pay = 42.10 * 2 * order_size
#     elif size == 'big':
#         to_pay = 24.80 * 5 * order_size
# elif fruit == 'Raspberry':
#     if size == 'small':
#         to_pay = 20 * 2 * order_size
#     elif size == 'big':
#         to_pay = 15.20 * 5 * order_size
#
# if to_pay >= 400 and to_pay <= 1000:
#     to_pay = 0.85 * to_pay
# elif to_pay > 1000:
#     to_pay = 0.5 * to_pay
#
# print(f'{to_pay:.2f} lv.')

# Zadacha 4

# food_bought = int(input()) * 1000
# command = input()
#
# while command != 'Adopted':
#     food_eaten = int(command)
#     food_bought -= food_eaten
#     command = (input())
#
# if food_bought >= 0:
#     print(f'Food is enough! Leftovers: {food_bought} grams.')
# elif food_bought < 0:
#     print(f'Food is not enough. You need {abs(food_bought)} grams more.')

# Zadacha 5

# project_parts = int(input())
# price_per_point = float(input())
# points_total = 0
#
# for part in range(1, project_parts + 1):
#     numbers_collected = int(input())
#     if part % 2 == 0:
#         numbers_collected *= 2
#     points_total += numbers_collected
#
# print(f'The project prize was {points_total * price_per_point:.2f} lv.')

# Zadacha 6

# a = int(input())
# b = int(input())
# max_num_pass = int(input())
# counter = 0
#
# while True:
#     first_sym = 35
#     second_sym = 64
#     for x in range(1, a + 1):
#         if counter == max_num_pass:
#             break
#         for y in range(1, b + 1):
#             print(f'{chr(first_sym)}{chr(second_sym)}{x}{y}{chr(second_sym)}{chr(first_sym)}|', end="")
#             first_sym += 1
#             if first_sym == 56:
#                 first_sym = 35
#             second_sym += 1
#             if second_sym == 97:
#                 second_sym = 64
#             counter += 1
#             if counter == max_num_pass:
#                 break
#     break

