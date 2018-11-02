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



budget = int(input())
season = input()
number_of_fisherman = int(input())

price = None


if season == 'Spring':
    price = 3000
    if number_of_fisherman <= 6:
        price -= 0.1 * price
    elif 6 < number_of_fisherman < 12:
        price -= 0.15 * price
    elif number_of_fisherman >= 12:
        price -= 0.25 * price
elif season == 'Summer' or season == 'Autumn':
    price = 4200
    if number_of_fisherman <= 6:
        price -= 0.1 * price
    elif 6 < number_of_fisherman < 12:
        price -= 0.15 * price
    elif number_of_fisherman >= 12:
        price -= 0.25 * price
elif season == 'Winter':
    price = 2600
    if number_of_fisherman <= 6:
        price -= 0.1 * price
    elif 6 < number_of_fisherman < 12:
        price -= 0.15 * price
    elif number_of_fisherman >= 12:
        price -= 0.25 * price


if not season == 'Autumn' and number_of_fisherman % 2 == 0:
    price -= 0.05 * price

left = budget - price

if left >= 0:
    print(f"Yes! You have {left:.2f} leva left.")
else:
    print(f"Not enough money! You need {abs(left):.2f} leva.")


# budget = int(input())
# season = input()
# fisherman = int(input())
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




