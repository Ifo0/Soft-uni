# #Zadacha 3
# x1 = float(input())
# y1 = float(input())
# x2 = float(input())
# y2 = float(input())
# x = float(input())
# y = float(input())
# # Check wether x and y are in the rectangle ...
#
# is_within_x_coordinates = x >= x1 and x <= x2
# is_within_y_coordinates = y >= y1 and y <= y2
#
# if is_within_x_coordinates and is_within_y_coordinates:
#     print('Inside')
# else:
#     print('Outside')

# Zadacha 6
# fruit = input().lower()
# day = input().lower()
# quantity = float(input())
#
# is_weekend = day == 'sunday' or day == 'saturday'
# is_workday = day == 'monday' or day == 'tuesday' or day == 'wednesday' or day == 'thursday' or day =='friday'
# valid_fruits = fruit == 'apple' or fruit == 'banana' or fruit == 'orange' or fruit == 'grapefruit' or fruit ==  'kiwi' or fruit ==  'pineapple' or fruit == 'grapes'
# # print(is_weekend)
# # print(is_workday)
# # print(valid_fruits)
#
# apple = 1.20
# banana = 2.50
# orange = 0.85
# grapefruit = 1.45
# kiwi = 2.70
# pineapple = 5.50
# grapes = 3.85
#
#
# to_pay = None
#
# if not (is_weekend or is_workday):
#     print('error')
# elif not valid_fruits:
#     print('error')
# else:
#     if not is_weekend:
#         to_pay = eval(fruit) * quantity
#     else:
#         if fruit == 'apple' or fruit == 'orange':
#             to_pay = (eval(fruit) + 0.05) * quantity
#         elif fruit == 'banana':
#             to_pay = (eval(fruit) + 0.20) * quantity
#         elif fruit == 'grapefruit':
#             to_pay = (eval(fruit) + 0.15) * quantity
#         elif fruit == 'kiwi':
#             to_pay = (eval(fruit) + 0.30) * quantity
#         elif fruit == 'pineapple':
#             to_pay = (eval(fruit) + 0.10) * quantity
#         elif fruit == 'grapes':
#             to_pay = (eval(fruit) + 0.35) * quantity
#     print(f'{to_pay:.2f}')

# Zadacha 7

# city = input()
# sales = float(input())
# comission = -1
#
# if city == 'Sofia':
#     if sales >= 0 and sales <= 500:
#         comission = 0.05
#     elif sales >= 500 and sales <= 1000:
#         comission = 0.07
#     elif sales >= 1000 and sales <= 10000:
#         comission = 0.08
#     elif salesl > 10000:
#         comission = 0.12
# elif city == 'Varna':
#     if sales >= 0 and sales <= 500:
#         comission = 0.045
#     elif sales >= 500 and sales <= 1000:
#         comission = 0.075
#     elif sales >= 1000 and sales <= 10000:
#         comission = 0.10
#     elif sales > 10000:
#         comission = 0.13
# elif city == 'Plovdiv':
#     if sales >= 0 and sales <= 500:
#         comission = 0.055
#     elif sales >= 500 and sales <= 1000:
#         comission = 0.08
#     elif sales >= 1000 and sales <= 10000:
#         comission = 0.12
#     elif sales > 10000:
#         comission = 0.145
#
# if comission == -1:
#         print('error')
# # elif sales <= 0:
# #         print('error')
# else:
#     print(f'{(comission * sales):.2f}')

#Zadacha 10

# budget = float(input())
# type_of_tickets = input().lower()
# size_of_group = int(input())
#
# transportation_cost = None
# budget_left = None
# ticket_cost = None
# balance = None
# vip_ticket = 499.99
# normal_ticket = 249.99
#
# if 1 <= size_of_group <= 4:
#     transportation_cost = 0.75 * budget
# elif 5 <= size_of_group <= 9:
#     transportation_cost = 0.6 * budget
# elif 10 <= size_of_group <= 24:
#     transportation_cost = 0.5 * budget
# elif 25 <= size_of_group <= 49:
#     transportation_cost = 0.4 * budget
# elif size_of_group >= 50:
#     transportation_cost = 0.25 * budget
#
# budget_left = budget - transportation_cost
#
# if type_of_tickets == 'vip':
#     ticket_cost = size_of_group * vip_ticket
# elif type_of_tickets == 'normal':
#     ticket_cost = size_of_group * normal_ticket
#
# balance = budget_left - ticket_cost
#
# if balance >= 0:
#     print(f'Yes! You have {balance:.2f} leva left.')
# elif balance < 0:
#     print(f'Not enough money! You need {abs(balance):.2f} leva.')

# def fibonacci(number):
#     if number == 1 or number == 2:
#         return 1
#     else:
#         return fibonacci(number - 1) + fibonacci(number - 2)
#
# if __name__ == '__main__':
#     print(fibonacci(10))

# Zadacha 1

# age = float(input())
# gender = input()
#
# if (age < 16):
#     if gender == 'f':
#         print('Miss')
#     else:
#         print('Master')
# else:
#     if gender == 'f':
#         print('Ms.')
#     else:
#         print('Mr.')

# Zadacha 2

# product = input()
# city = input()
# quantity = float(input())
#
# if city == 'Sofia':
#     if product == 'coffee':
#         print(f"{0.50 * quantity}")
#     elif product == 'water':
#         print(f"{0.80 * quantity}")
#     elif product == 'beer':
#         print(f"{1.20 * quantity}")
#     elif product == 'sweets':
#         print(f"{1.45 * quantity}")
#     elif product == 'peanuts':
#         print(f"{1.60 * quantity}")
# elif city == 'Plovdiv':
#     if product == 'coffee':
#         print(f"{0.40 * quantity}")
#     elif product == 'water':
#         print(f"{0.70 * quantity}")
#     elif product == 'beer':
#         print(f"{1.15 * quantity}")
#     elif product == 'sweets':
#         print(f"{1.30 * quantity}")
#     elif product == 'peanuts':
#         print(f"{1.50 * quantity}")
# elif city == 'Varna':
#     if product == 'coffee':
#         print(f"{0.45 * quantity}")
#     elif product == 'water':
#         print(f"{0.70 * quantity}")
#     elif product == 'beer':
#         print(f"{1.10 * quantity}")
#     elif product == 'sweets':
#         print(f"{1.35 * quantity}")
#     elif product == 'peanuts':
#         print(f"{1.55 * quantity}")

# Zadacha 4
#
# product = input()
#
# fruits = ['banana', 'apple', 'kiwi', 'cherry', 'lemon', 'grapes']
# vegetables = ['tomato', 'cucumber', 'pepper', 'carrot']
#
#
# if product in fruits:
#     print('fruit')
# elif product in vegetables:
#     print('vegetable')
# else:
#     print('unknown')


#Zadacha 5

# number = int(input())
#
# if not number in range(100, 201) and not number == 0:
#     print('invalid')

#Zadacha  8
# number = int(input())
#
# days = ['Placeholder', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
#
# if number >= 1 and number <= 7:
#     print(days[number])
# else:
#     print('Error')

#Zadacha 9

# vhod = input()
# dict = {'mamal': 'dog', 'reptile': ['crocodile', 'tortoise', 'snake']}
#
# if vhod in dict.values()
#     print(dict.key)
#
# vhod = input()
#
# if vhod == 'dog':
#     print('mammal')
# elif vhod == 'crocodile' or vhod == 'tortoise' or vhod == 'snake':
#     print('reptile')
# else:
#     print('unknown')


