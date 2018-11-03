#Zadacha 1
#
# x1 = float(input())
# y1 = float(input())
# x2 = float(input())
# y2 = float(input())
# x = float(input())
# y = float(input())
#
#
# if x == x1 or x == x2:
#     if y >= y1 and y <= y2:
#         print('Border')
#     else:
#         print('Inside / Outside')
# elif y == y1 or y == y2:
#     if x >= x1 and x <= x2:
#         print('Border')
#     else:
#         print('Inside / Outside')
# else:
#     print('Inside / Outside')

# Zadacha 2

# Premiere = 12.00
# Normal = 7.50
# Discount = 5.00
#
# x = input()
# r = int(input())
# c = int(input())
#
# income = r * c * (eval(x))
#
# print(f'{income:.2f} leva')

# Zadacha 3
# import math
# year = input()
# public_holidays = int(input())
# weekends_at_home = int(input())
#
# weekends_a_year = 48
# weekends_at_sofia = weekends_a_year - weekends_at_home
#
# play_in_sofia = (3 / 4) * weekends_at_sofia + (2 / 3) * public_holidays
# total_play = play_in_sofia + weekends_at_home
#
# if year == 'leap':
#     total_play *= 1.15
#     print(f'{math.floor(total_play):.0f}')
# else:
#     print(f'{math.floor(total_play):.0f}')

# Zadacha 4
# temp = int(input())
# time_of_day = input()
#
# if 10 <= temp <= 18:
#     if time_of_day == 'Morning':
#         print(f"It's {temp} degrees, get your Sweatshirt and Sneakers.")
#     elif time_of_day == 'Afternoon' or time_of_day == 'Evening':
#         print(f"It's {temp} degrees, get your Shirt and Moccasins.")
# elif 18 < temp <= 24:
#     if time_of_day == 'Morning' or time_of_day == 'Evening':
#         print(f"It's {temp} degrees, get your Shirt and Moccasins.")
#     elif time_of_day == 'Afternoon':
#         print(f"It's {temp} degrees, get your T-Shirt and Sandals.")
# elif temp >= 25:
#     if time_of_day == 'Morning':
#         print(f"It's {temp} degrees, get your T-Shirt and Sandals.")
#     elif time_of_day == 'Afternoon':
#         print(f"It's {temp} degrees, get your Swim Suit and Barefoot.")
#     elif time_of_day == 'Evening':
#         print(f"It's {temp} degrees, get your Shirt and Moccasins.")
#

# Zadacha 5

# flower = input()
# number_of_flowers = int(input())
# budget = int(input())
#
# Roses = 5
# Dahlias = 3.80
# Tulips = 2.80
# Narcissus = 3
# Gladiolus = 2.50
# price = None
#
#
# if flower == 'Roses':
#     if number_of_flowers > 80:
#         price = eval(flower) * number_of_flowers * 0.9
#     else:
#         price = eval(flower) * number_of_flowers
# elif flower == 'Dahlias':
#     if number_of_flowers > 90:
#         price = eval(flower) * number_of_flowers * 0.85
#     else:
#         price = eval(flower) * number_of_flowers
# elif flower == 'Tulips':
#     if number_of_flowers > 80:
#         price = eval(flower) * number_of_flowers * 0.85
#     else:
#         price = eval(flower) * number_of_flowers
# elif flower == 'Narcissus':
#     if number_of_flowers < 120:
#         price = eval(flower) * number_of_flowers * 1.15
#     else:
#         price = eval(flower) * number_of_flowers
# elif flower == 'Gladiolus':
#     if number_of_flowers < 80:
#         price = eval(flower) * number_of_flowers * 1.20
#     else:
#         price = eval(flower) * number_of_flowers
#
# if price <= budget:
#     print(f"Hey, you have a great garden with {number_of_flowers} {flower} and {budget - price:.2f} leva left.")
# elif price > budget:
#     print(f"Not enough money, you need {price - budget:.2f} leva more.")


#Zadacha 6



# budget = int(input())
# season = input()
# number_of_fisherman = int(input())
#
# price = None
#
#
# if season == 'Spring':
#     price = 3000
#     if number_of_fisherman <= 6:
#         price -= 0.1 * price
#     elif 6 < number_of_fisherman < 12:
#         price -= 0.15 * price
#     elif number_of_fisherman >= 12:
#         price -= 0.25 * price
# elif season == 'Summer' or season == 'Autumn':
#     price = 4200
#     if number_of_fisherman <= 6:
#         price -= 0.1 * price
#     elif 6 < number_of_fisherman < 12:
#         price -= 0.15 * price
#     elif number_of_fisherman >= 12:
#         price -= 0.25 * price
# elif season == 'Winter':
#     price = 2600
#     if number_of_fisherman <= 6:
#         price -= 0.1 * price
#     elif 6 < number_of_fisherman < 12:
#         price -= 0.15 * price
#     elif number_of_fisherman >= 12:
#         price -= 0.25 * price
#
#
# if not season == 'Autumn' and number_of_fisherman % 2 == 0:
#     price -= 0.05 * price
#
# left = budget - price
#
# if left >= 0:
#     print(f"Yes! You have {left:.2f} leva left.")
# else:
#     print(f"Not enough money! You need {abs(left):.2f} leva.")
#

# budget = int(input())
# season = input()
# fisherman = int(input())
#
# Zadacha 7
#
# Spring = 3000
# Summer = Autumn = 4200
# Winter = 2600
#
# if fisherman <= 6:
#     discount = 0.1
# elif fisherman > 6 and fisherman < 12:
#     discount = 0.15
# elif fisherman >= 12:
#     discount = 0.25
#
# if fisherman % 2 == 0:
#     if season == 'Spring' or season == 'Summer' or season == 'Winter':
#        discount += 0.05
#
# discount_sum = eval(season) * discount
# price = eval(season) - discount_sum
# left = abs(price - budget)
#
# if budget >= price:
#     print(f"Yes! You have {left:.2f} leva left.")
# elif price > budget:
#     print(f"Not enough money! You need {left:.2f} leva.")

#Zadacha 8

# budget = float(input())
# season = input()
#
# destination = None
# facility = None
# expenditure = None
#
# if budget <= 100:
#     destination = 'Bulgaria'
#     if season == 'summer':
#         facility = 'Camp'
#         proportion = 0.3
#         expenditure = proportion * budget
#     elif season == 'winter':
#         facility = 'Hotel'
#         proportion = 0.7
#         expenditure = proportion * budget
# elif 100 < budget <= 1000:
#     destination = 'Balkans'
#     if season == 'summer':
#         facility = 'Camp'
#         proportion = 0.4
#         expenditure = proportion * budget
#     elif season == 'winter':
#         facility = 'Hotel'
#         proportion = 0.8
#         expenditure = proportion * budget
# elif budget > 1000:
#     destination = 'Europe'
#     facility = 'Hotel'
#     proportion = 0.9
#     expenditure = proportion * budget
#
# print(f"Somewhere in {destination}")
# print(f"{facility} - {expenditure:.2f}")

#Zadacha 9

# n1 = int(input())
# n2 = int(input())
# operator = input()
#
# result = None
# even_odd = None
#
# if n2 == 0:
#     print(f"Cannot divide {n1} by zero")
# elif operator == '+' or operator == '*' or operator == '-':
#     if operator == '+':
#         result = n1 + n2
#     elif operator == '*':
#         result = n1 * n2
#     elif operator == '-':
#         result = n1 - n2
#     if result % 2 == 0:
#         even_odd = 'even'
#     else:
#         even_odd = 'odd'
#     print(f"{n1} {operator} {n2} = {result} - {even_odd}")
# elif operator == '/':
#     result = n1 / n2
#     print(f"{n1} / {n2} = {result:.2f}")
# elif operator == '%':
#     result = n1 % n2
#     print(f"{n1} % {n2} = {result}")

#Zadacha 10
month = input()
lenght_of_stay = int(input())

cost_of_stay = None

if month == 'May' or month == 'October':
    ppn_s = 50
    ppn_a = 65
    cost_of_stay_s = lenght_of_stay * ppn_s
    cost_of_stay_a = lenght_of_stay * ppn_a
    if lenght_of_stay > 7 and lenght_of_stay <= 14:
        cost_of_stay_s -= 0.05 * cost_of_stay_s
    elif lenght_of_stay > 14:
        cost_of_stay_s -= 0.3 * cost_of_stay_s
        cost_of_stay_a -= 0.1 * cost_of_stay_a
elif month == 'June' or month == 'September':
    ppn_s = 75.20
    ppn_a = 68.70
    cost_of_stay_s = lenght_of_stay * ppn_s
    cost_of_stay_a = lenght_of_stay * ppn_a
    if lenght_of_stay > 14:
        cost_of_stay_s -= 0.2 * cost_of_stay_s
        cost_of_stay_a -= 0.1 * cost_of_stay_a
elif month == 'June' or month == 'September':
    ppn_s = 75.20
    ppn_a = 68.70
    cost_of_stay_s = lenght_of_stay * ppn_s
    cost_of_stay_a = lenght_of_stay * ppn_a
    if lenght_of_stay > 14:
        cost_of_stay_s -= 0.2 * cost_of_stay_s
        cost_of_stay_a -= 0.1 * cost_of_stay_a
elif month == 'July' or month == 'August':
    ppn_s = 76
    ppn_a = 77
    cost_of_stay_s = lenght_of_stay * ppn_s
    cost_of_stay_a = lenght_of_stay * ppn_a
    if lenght_of_stay > 14:
        cost_of_stay_a -= 0.1 * cost_of_stay_a

print(f"Apartment: {cost_of_stay_a:.2f} lv.")
print(f"Studio: {cost_of_stay_s:.2f} lv.")


