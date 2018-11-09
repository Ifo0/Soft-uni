# Zadacha 1

# a = int(input())
# b = int(input())
# c = None
#
# while not b == 0:
#     c = b
#     b = a % b
#     a = c
#
# print(a)

# Zadacha 2
# book = input()
# libsize = int(input())
# checked_book = None
# counter = 0
# found = False
#
# while counter < libsize:
#     checked_book = input()
#     if checked_book == book:
#         print(f'You checked {counter} books and found it.')
#         found = True
#         break;
#     counter += 1
#
# if found == False:
#     print(f'The book you search is not here!')
#     print(f'You checked {counter} books.')

# Zadacha 3

# unsatisfactory = int(input())
#
# count_bad = 0
# count_all = 0
# sum_all_grades = 0
# last_exercise = ''
#
# exercise_name = input()
# while not exercise_name == 'Enough':
#     grade = int(input())
#     last_exercise = exercise_name
#     sum_all_grades += grade
#     count_all += 1
#     if grade <= 4:
#         count_bad += 1
#         if count_bad == unsatisfactory:
#             break
#     exercise_name = input()
#
# if exercise_name == 'Enough':
#     print(f'Average score: {sum_all_grades / count_all:.2f}')
#     print(f'Number of problems: {count_all}')
#     print(f'Last problem: {last_exercise}')
# else:
#     print(f'You need a break, {count_bad} poor grades.')


# Zadacha 4

# Reworked solution
# cost_of_trip = float(input())
# available_money = float(input())
# money = ''
# days_passed = 0
# spending_counter = 0
#
# while cost_of_trip > available_money:
#     action = input()
#     money = float(input())
#     if action == 'save':
#         spending_counter = 0
#         available_money += money
#     elif action == 'spend':
#         spending_counter += 1
#         available_money -= money
#         if available_money < 0:
#             available_money = 0
#     days_passed += 1
#     if spending_counter == 5:
#         break
#
#
# if cost_of_trip <= available_money:
#     print(f'You saved the money for {days_passed} days.')
# else:
#     print("You can't save the money.")
#     print(f'{days_passed}')

######## Original mine
# Problem was that I was making a strict comparisson for available money
# to be equal to cost of trip, wheras they could exceed.

# cost_of_trip = float(input())
# available_money = float(input())
# saved = ''
# spent = ''
# days_passed = 0
# spending_counter = 0
#
# while True:   #not available_money == cost_of_trip:
#     action = input()
#     days_passed += 1
#     if action == 'save':
#         spending_counter = 0
#         saved = float(input())
#         available_money += saved
#         if available_money >= cost_of_trip:
#             print(f'You saved the money for {days_passed} days.')
#             break
#     elif action == 'spend':
#         spending_counter += 1
#         spent = float(input())
#         if spent > available_money:
#             available_money = 0
#         else:
#             available_money -= spent
#
#         if spending_counter == 5:
#             print("You can't save the money.")
#             print(f'{days_passed}')
#             break

# Zadacha 5
#
# change = float(input()) * 100
#
#
# penny = 1
# two_penny = 2
# five_penny = 5
# ten_penny = 10
# one_fifth = 20
# half = 50
# one = 100
# two = 200
#
# coins_returned = 0
#
# while change > 0:
#     if not change / two == 0:
#         coins_returned += change // two
#         change = change % two
#     if not change / one == 0:
#         coins_returned += change // one
#         change = change % one
#     if not change / half == 0:
#         coins_returned += change // half
#         change = change % half
#     if not change / one_fifth == 0:
#         coins_returned += change // one_fifth
#         change = change % one_fifth
#     if not change / ten_penny == 0:
#         coins_returned += change // ten_penny
#         change = change % ten_penny
#     if not change / five_penny == 0:
#         coins_returned += change // five_penny
#         change = change % five_penny
#     if not change / two_penny == 0:
#         coins_returned += change // two_penny
#         change = change % two_penny
#     if not change / penny == 0:
#         coins_returned += change // penny
#         change = change % penny
#     break
#
# print(f'{coins_returned:.0f}')
#

# Zadacha 6
#
# length = int(input())
# width = int(input())
#
# area = length * width
# area_const = area
# action = ''
# action_sum = 0
#
#
# while area >= 0:
#     action = input()
#     if not action == 'STOP':
#         action = int(action)
#         area -= action
#         action_sum += action
#     else:
#         left = area_const - action_sum
#         print(f'{left} pieces are left.')
#         break
#
# if not action == 'STOP':
#     print(f'No more cake left! You need {abs(area)} pieces more.')



