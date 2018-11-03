#Zadacha 1

# number = int(input())
#
# while number < 1 or number > 100:
#     print('invalid number')
#     number = int(input())
#
# print(f'The number is: {number}')

# number = int(input())
#
# while not (number >= 1 and  number <= 100):
#     print('invalid number')
#     number = int(input())
#
# print(f'The number is: {number}')


# Zadacha 2:
# name = input()
# sr_uspeh = 0
# counter = 1
# while counter <= 12:
#     ocenka = float(input())
#     if ocenka >= 4.00:
#         sr_uspeh += ocenka
#         counter += 1
#     else:
#         continue
#
# print(f'{name} graduated. Average grade: {sr_uspeh / 12:.2f}')

#Zadacha 3


#Zadacha 4
# command = input()
# largest = int(command)
# smallest = int(command)
#
# while not command == 'END':
#     number = int(command)
#     if smallest > number:
#         smallest = number
#     if largest < number:
#         largest = number
#     command = input()
#
# print(f"Max number: {largest}")
# print(f"Min number: {smallest}")



# Zadacha 5
# goal = 10000
# counter = 0
# while counter < goal:
#     command = input()
#     if not command == 'Going home':
#         steps = int(command)
#         counter += steps
#         if counter >= goal:
#             print(f"Goal reached! Good job!")
#             break
#         # command = input()
#     if command == 'Going home':
#         steps = input()
#         steps = int(steps)
#         counter += steps
#         if counter >= goal:
#             print(f"Goal reached! Good job!")
#             break
#         else:
#             diff = goal - counter
#             print(f'{diff:.0f} more steps to reach goal.')
#             break






# Zadacha 6
# deposits = int(input())
#
# sum = 0
# counter = 0
#
# while counter < deposits:
#     transaction = float(input())
#     if transaction < 0:
#         print(f"Invalid operation!")
#         break
#     print(f"Increase: {transaction:.2f}")
#     sum += transaction
#     counter += 1
#
#
# print(f"Total: {sum:.2f}")


#Zadacha 7
# volume = int(input())
#
# Easy = 50
# Medium = 100
# Hard = 200
# taps = 0
# filled = 0
#
# while filled < volume:
#     type_of_tap = input()
#
#     filled += eval(type_of_tap)
#     taps += 1
#
# if filled <= volume:
#     print(f"The dispenser has been tapped {taps} times.")
# elif filled > volume:
#     print(f"{filled - volume}ml has been spilled.")


# Zadacha 8
# seek = int(input())
#
# numbers = 1
# print(numbers)
#
# while numbers < seek:
#     numbers = 2 * numbers + 1
#     if numbers > seek:
#         break
#     else:
#         print(numbers)

#Last exersice

# width = int(input())
# length = int(input())
# height = int(input())
#
# free_space = width * length * height
#
# box = input()
# count_box = 0
#
# while not box == 'Done':
#     count_box += int(box)
#     if count_box >= free_space:
#         break
#     box = input()
#
# diff = free_space - count_box
#
# if diff >= 0:
#     print(f"{diff} Cubic meters left.")
# elif diff < 0:
#     print(f"No more free space! You need {abs(diff)} Cubic meters more.")
