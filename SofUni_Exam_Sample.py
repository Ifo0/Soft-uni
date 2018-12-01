# # Zadacha 1
#
# distance = 420
# fuel_consumption = 7/100
# fuel_price = 1.85
# fuel_consumed = 7/100 * distance
# fuel_total = fuel_consumed * 1.85
#
# food_day = float(input())
# souv_day = float(input())
# hotel_day = float(input())
#
# hotel_day1 = 0.9 * hotel_day
# hotel_day2 = 0.85 * hotel_day
# hotel_day3 = 0.8 * hotel_day
#
# total_expenditure = hotel_day1 + hotel_day2 + hotel_day3 + fuel_total + 3*(food_day + souv_day)
#
# print(f'Money needed: {total_expenditure:.2f}')

# Zadacha 2
# import math
# width = float(input())
# length = float(input())
# height = float(input())
# average_person_height = float(input())
#
# volume_room = 2 * 2 * (average_person_height + 0.40)
# volume_spacecraft = width * length * height
#
# capacity = volume_spacecraft / volume_room
#
# if capacity >= 3 and capacity <= 10:
#     print(f'The spacecraft holds {math.floor(capacity)} astronauts.')
# elif capacity < 3:
#     print(f'The spacecraft is too small.')
# else:
#     print(f'The spacecraft is too big.')


# import math
# sushi = input()
# restaurant = input()
# portions = int(input())
# delivery = input()
# price_order = 0
# invalid = False
#
# if restaurant == 'Sushi Zone':
#     if sushi == 'sashimi':
#         price_order += 4.99
#     elif sushi == 'maki':
#         price_order += 5.29
#     elif sushi == 'uramaki':
#         price_order += 5.99
#     elif sushi == 'temaki':
#         price_order += 4.29
# elif restaurant == 'Sushi Time':
#     if sushi == 'sashimi':
#         price_order += 5.49
#     elif sushi == 'maki':
#         price_order += 4.69
#     elif sushi == 'uramaki':
#         price_order += 4.49
#     elif sushi == 'temaki':
#         price_order += 5.19
# elif restaurant == 'Sushi Bar':
#     if sushi == 'sashimi':
#         price_order += 5.25
#     elif sushi == 'maki':
#         price_order += 5.55
#     elif sushi == 'uramaki':
#         price_order += 6.25
#     elif sushi == 'temaki':
#         price_order += 4.75
# elif restaurant == 'Asian Pub':
#     if sushi == 'sashimi':
#         price_order += 4.50
#     elif sushi == 'maki':
#         price_order += 4.80
#     elif sushi == 'uramaki':
#         price_order += 5.50
#     elif sushi == 'temaki':
#         price_order += 5.50
# else:
#     print(f'{restaurant} is invalid restaurant!')
#     invalid = True
#
# if invalid is False:
#     order_total = price_order * portions
#     if delivery == 'Y':
#         delivery_price = 0.2 * order_total
#         order_total += delivery_price
#     print(f'Total price: {math.ceil(order_total)} lv.')


# Zadacha 4

# budget = float(input())
#
# spendings = 0
# balloons = 0.1
# flowers = 1.5
# candles = 0.5
# ribbon = 2
#
# balloons_quantity = 0
# flowers_quantity = 0
# candles_quantity = 0
# ribbon_metres = 0
#
# goods = input()
#
# while goods != 'stop':
#     quantity = int(input())
#     if goods == 'balloons':
#         balloons_quantity += quantity
#         spendings += eval(goods) * quantity
#     elif goods == 'flowers':
#         flowers_quantity += quantity
#         spendings += eval(goods) * quantity
#     elif goods == 'candles':
#         candles_quantity += quantity
#         spendings += eval(goods) * quantity
#     elif goods == 'ribbon':
#         ribbon_metres += quantity
#         spendings += eval(goods) * quantity
#     if spendings >= budget:
#         print(f'All money is spent!')
#         break
#     goods = input()
#
# if goods == 'stop':
#         print(f'Spend money: {spendings:.2f}')
#         print(f'Money left: {budget - spendings:.2f}')
#
# print(f'Purchased decoration is {balloons_quantity} balloons, {ribbon_metres} m ribbon, {flowers_quantity} flowers and {candles_quantity} candles.')



# Zadacha 5
# passengers = int(input())
# bus_stops = int(input())
# stops = 0
# incoming = 0
# outgoing = 0
#
# for i in range(bus_stops):
#     outgoing += int(input())
#     incoming += int(input())
#     stops += 1
#
# end_passangers = passengers + incoming - outgoing
#
# if stops % 2 != 0:
#     end_passangers += 2
#
# print(f'The final number of passengers is : {end_passangers}')

# Zadacha 6

# number = input()
#
#
# for first in range(1, int(number[-1]) + 1):
#     for second in range(1, int(number[-2]) + 1):
#         for third in range(1, int(number[-3]) + 1):
#             print(f'{first} * {second} * {third} = {first * second * third};')