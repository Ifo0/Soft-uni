# Zadacha 1

    # sectors = int(input())
    # total_capacity = int(input())
    # price_ticket = float(input())
    #
    # price_stadium = total_capacity * price_ticket
    # price_per_sector = price_stadium / sectors
    #
    # diff_total_sector = price_stadium - 0.75 * price_per_sector
    # charity = (1/8) * diff_total_sector
    #
    # print(f'Total income - {price_stadium:.2f} BGN')
    # print(f'Money for charity - {charity:.2f} BGN')


# Zadacha 2
# import math
#
# fan_name = input()
# budget = float(input())
# beers = int(input())
# chips = int(input())
#
# price_beer = 1.20
# total_beer = beers * price_beer
# price_chips =(total_beer * 0.45)
# total_chips = math.ceil(chips * price_chips)
# expenditure = total_beer + total_chips
#
# if expenditure <= budget:
#     print(f'{fan_name} bought a snack and has {budget - expenditure:.2f} leva left.')
# else:
#     print(f'{fan_name} needs {expenditure - budget:.2f} more leva!')


# Zadacha 3
# team = input()
# souvenier = input()
# sov_bought = int(input())
# expenditure = 0
#
# if team == 'Argentina':
#     if souvenier == 'flags':
#         expenditure = 3.25 * sov_bought
#     elif souvenier == 'caps':
#         expenditure = 7.20 * sov_bought
#     elif souvenier == 'posters':
#         expenditure = 5.10 * sov_bought
#     elif souvenier == 'stickers':
#         expenditure = 1.25 * sov_bought
#     else:
#         print(f'Invalid stock!')
# elif team == 'Brazil':
#     if souvenier == 'flags':
#         expenditure = 4.20 * sov_bought
#     elif souvenier == 'caps':
#         expenditure = 8.50 * sov_bought
#     elif souvenier == 'posters':
#         expenditure = 5.35 * sov_bought
#     elif souvenier == 'stickers':
#         expenditure = 1.20 * sov_bought
#     else:
#         print(f'Invalid stock!')
# elif team == 'Croatia':
#     if souvenier == 'flags':
#         expenditure = 2.75 * sov_bought
#     elif souvenier == 'caps':
#         expenditure = 6.90 * sov_bought
#     elif souvenier == 'posters':
#         expenditure = 4.95 * sov_bought
#     elif souvenier == 'stickers':
#         expenditure = 1.10 * sov_bought
#     else:
#         print(f'Invalid stock!')
# elif team == 'Denmark':
#     if souvenier == 'flags':
#         expenditure = 3.10 * sov_bought
#     elif souvenier == 'caps':
#         expenditure = 6.50 * sov_bought
#     elif souvenier == 'posters':
#         expenditure = 4.80 * sov_bought
#     elif souvenier == 'stickers':
#         expenditure = 0.90 * sov_bought
#     else:
#         print(f'Invalid stock!')
# else:
#     print(f'Invalid country!')
#
# if expenditure > 0:
#     print(f'Pepi bought {sov_bought} {souvenier} of {team} for {expenditure:.2f} lv.')


# Zadacha 4

# team = input()
# played_games = int(input())
# points = 0
# total_scored = 0
# total_taken = 0
#
#
# for game in range(played_games):
#     scored = 0
#     goals_taken = 0
#     scored += int(input())
#     goals_taken += int(input())
#     total_scored += scored
#     total_taken += goals_taken
#     if scored > goals_taken:
#         points += 3
#     elif scored == goals_taken:
#         points += 1
#
# if total_scored >= total_taken:
#     print(f"{team} has finished the group phase with {points} points.\nGoal difference: {total_scored - total_taken}.")
# else:
#     print(f"{team} has been eliminated from the group phase.\nGoal difference: {total_scored - total_taken}.")

# Zadacha 5
# budget = int(input())
# items = int(input())
# hoodie = 30
# keychain = 4
# tshirt = 20
# flag = 15
# sticker = 1
# expenditure = 0
#
# for i in range(items):
#     item = input()
#     if item == 'T-shirt':
#         expenditure += tshirt
#     else:
#         expenditure += eval(item)
#
# if budget >= expenditure:
#     print(f'You bought {items} items and left with {budget - expenditure} lv.')
# else:
#     print(f'Not enough money, you need {expenditure - budget} more lv.')

# Zadacha 6

combination = int(input())
counter = 0


for letter in range(ord("B"), ord("L")+1, 2):
    for letter2 in range(ord("f"), ord("a")-1, -1):
        for letter3 in range(ord("A"), ord("C")+1):
            for number in range(1, 11):
                for number2 in range(10, 0, -1):
                    counter += 1
                    if counter == combination:
                        print(f'Ticket combination: {chr(letter)}{chr(letter2)}{chr(letter3)}{number}{number2}')
                        sum_prize = letter + letter2 + letter3 + number + number2
                        print(f'Prize: {sum_prize} lv.')


