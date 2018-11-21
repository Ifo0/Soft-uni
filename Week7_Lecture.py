# for hour in range(0, 24):
#     for minutes in range (1, 60):
#         for seconds in range(1, 60):
#             print(f'{hour}:{minutes}:{seconds}')


# Zadacha 1
# n = int(input())
#
# for i in range(n, 0, -1):
#     print(i)

# Zadacha 2
# n = int(input())
#
# for i in range(1, n+1, 3):
#     print(i)

# Zadacha 3:
# n = int(input())
#
# for i in range(0, n+1):
#     if i % 2 == 0:
#         print(2**i)


# Zadacha 4:
# floors = int(input())
# rooms = int(input())
# last_floor = True
#
# for floor in range(floors, 0, -1):
#     for room in range(0, rooms):
#         if last_floor == True:
#             print(f'L{floor}{room} ', end="")
#         else:
#             if floor % 2 == 0:
#                 print(f'O{floor}{room} ', end="")
#             else:
#                 print(f'A{floor}{room} ', end="")
#     last_floor = False
#     print()

# Zadacha 5
# solution = int(input())
# a = b = c = d = e = 0
# equation = a + b + c + d + e
# count = 0
#
# for a in range(0, solution+1):
#     for b in range(0, solution+1):
#         for c in range(0, solution+1):
#             for d in range(0, solution+1):
#                 for e in range(0, solution+1):
#                     equation = a + b + c + d + e
#                     if equation == solution:
#                         count += 1
#
# print(count)


# Zadacha 6
# destination = input()
# sum_needed = float(input())
# saved = 0
#
# while True:
#     user_input = float(input())
#     saved += user_input
#     if saved >= sum_needed:
#         print(f'Going to {destination}!')
#         destination = input()
#         if destination == 'End':
#             break
#         sum_needed = float(input())
#         saved = 0

#
#
#
# saved = 0
# while True:
#     destination = input()
#     if destination == 'End':
#         break
#     sum_needed = float(input())
#     while saved < sum_needed:
#         saved += float(input())
#     print(f'Going to {destination}!')
#     saved = 0


# Zadacha 7


# max_sum = 0
# ascii_sum = 0
# winner = ''
#
# while True:
#     name = input()
#     if name == 'STOP':
#         print(f'Winner is {winner} - {max_sum}!')
#         break
#     ascii_sum = 0
#     for letter in name:
#         ascii_sum += ord(letter)
#         if ascii_sum > max_sum:
#             winner = name
#             max_sum = ascii_sum

# Zadacha 8

# order_size = int(input())
# product = ''
#
# count = 0
#
# for batch in range(1, order_size+1):
#     flour = False
#     sugar = False
#     eggs = False
#     while True:
#         product = input()
#         if product == 'flour':
#             flour = True
#         elif product == 'sugar':
#             sugar = True
#         elif product == 'eggs':
#             eggs = True
#         elif product == 'Bake!':
#             if flour is True and sugar is True and eggs is True:
#                 print(f'Baking batch number {batch}...')
#                 break
#             else:
#                 print(f'The batter should contain flour, eggs and sugar!')

#
# order_size = int(input())
# product = ''
# flour = False ## For this version to be right, these three need to also be copied after the print Baking batch number ....
# sugar = False
# eggs = False
# count = 0
#
# while not count == order_size:
#     product = input()
#     if product == 'flour':
#         flour = True
#     elif product == 'sugar':
#         sugar = True
#     elif product == 'eggs':
#         eggs = True
#     elif product == 'Bake!':
#         if flour is True and sugar is True and eggs is True:
#             count += 1
#             print(f'Baking batch number {count}...')
#         else:
#             print(f'The batter should contain flour, eggs and sugar!')


# Zadacha 9

# magic_num = int(input())
# product = 0
#
# for a in range(1, 10):
#     for b in range(1, 10):
#         for c in range(1, 10):
#             for d in range(1, 10):
#                 for e in range(1, 10):
#                     for f in range(1, 10):
#                         product = a * b * c * d * e * f
#                         if product == magic_num:
#                             print(f'{a}{b}{c}{d}{e}{f} ', end = "")



