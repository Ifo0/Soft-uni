# Zadacha 1
# a = int(input())
# b = int(input())
# c = int(input())
# d = int(input())
#
# for integer1 in range(a, b+1):
#     for integer2 in range(a, b+1):
#         for integer3 in range(c, d+1):
#             for integer4 in range(c, d+1):
#                 if integer1 + integer4 == integer2 + integer3 \
#                         and not integer1 == integer2 \
#                         and not integer3 == integer4:
#                     print(f'{integer1}{integer2}\n{integer3}{integer4}\n')

# Zadacha 2
# import sys
# n = int(input())
# number = 1
# numbers_printed = 0
# row_number = 1
#
# while True:
#     while not numbers_printed == row_number:
#         print(number, end=" ")
#         number += 1
#         if number > n:
#             sys.exit(0)
#         numbers_printed += 1
#     print()
#     row_number += 1
#     numbers_printed = 0



# Zadacha 3

# n = int(input())
# number = 0
#
# for row in range(1, n+1):
#     number = row
#     backwards = False
#     for col in range(1, n+1):
#         print(number, end="")
#         if number == n or backwards is True:
#             backwards = True
#             number -= 1
#         else:
#             number += 1
#     print()

# n = int(input())
# number = 0
#
# for row in range(1, n+1):
#     number = row
#     backwards = False
#     for col in range(1, n+1):
#         print(number, end=" ")
#         if number == n:
#             backwards = True
#         if backwards is True:
#             number -= 1
#         else:
#             number += 1
#     print()


# SoftUni sol to above
# n = int(input())
# current = 1
#
# for row in range(0, n):
#     for col in range(0, n):
#         current = row + col + 1
#         if current > n:
#             current = 2*n - current
#         print(current, end = "")
#     print()
#

# Zadacha 4
# n = int(input())
# n_string = str(n)
# n_len = len(n_string)
# char = -1
#
# for row in range(0, n_len):
#     n_string_integer = int(n_string[char])
#     if n_string_integer is 0:
#         print('ZERO', end="")
#     else:
#         for column in range(n_string_integer):
#             character = chr(n_string_integer + 33)
#             print(character, end="")
#     char -= 1
#     print()

#Softuni
# n = input()
# for i in reversed(n):
#     if i == 0:
#         print('Zero')
#     else:
#         symbol = int(i) + 33
#         symbol = chr(symbol)
#         print(symbol * int(i))




# Zadacha 5
# m = int(input())
# n = int(input())
#
#
# for number in range(m, n+1):
#     original_value = number
#     sum_even = 0
#     sum_odd = 0
#     for integer in range(6):
#         modulo_even = number % 10
#         sum_even += modulo_even
#         number = number // 10
#         modulo_odd = number % 10
#         sum_odd += modulo_odd
#         number = number // 10
#     if sum_even == sum_odd:
#         print(original_value, end=" ")


# m = input()
# n = input()
#
# for number in range(int(m), int(n) + 1):
#     sum_even = 0
#     sum_odd = 0
#     for index, num in enumerate(str(number), start = 1):
#         if index % 2 == 0:
#             sum_odd += int(num)
#         else:
#             sum_even += int(num)
#     if sum_even == sum_odd:
#         print(number, end=" ")


# Zadacha 6
#
# m = input()
# n = input()
#
# for number in range(int(m), int(n)+1):
#     number = str(number)
#     left = int(number[0]) + int(number[1])
#     right = int(number[-1]) + int(number[-2])
#     middle = int(number[2])
#     diff = left - right
#     if left is right:
#         print(number, end= " ")
#     else:
#         if diff > 0:
#             right += middle
#             if right is left:
#                 print(number, end=" ")
#         else:
#             left += middle
#             if left is right:
#                 print(number, end=" ")




# Zadacha 7

# not_primes = 0
# primes = 0
#
# while True:
#     item = input()
#     if item != 'stop':
#         item = int(item)
#         if item < 0:
#             print('Number is negative.')
#         else:
#             prime_checker = True #We assume that the input is a prime number, unless proven otherwise
#             for number in range(2, item):
#                 if item is not number and item % number == 0:
#                     prime_checker = False # prove input is not a prime number
#                     break
#             if prime_checker is True:
#                 primes += item
#             else:
#                 not_primes += item
#     else:
#         print(f'Sum of all prime numbers is: {primes}')
#         print(f'Sum of all non prime numbers is: {not_primes}')
#         break

# def is_prime(n):
#   if n == 2 or n == 3: return True
#   if n < 2 or n%2 == 0: return False
#   if n < 9: return True
#   if n%3 == 0: return False
#   r = int(n**0.5)
#   f = 5
#   while f <= r:
#     if n%f == 0: return False
#     if n%(f+2) == 0: return False
#     f +=6
#   return True
#
#
# not_primes = 0
# primes = 0
#
# while True:
#     item = input()
#     if item != 'stop':
#         item = int(item)
#         if item < 0:
#             print('Number is negative.')
#         else:
#             if is_prime(item):
#                 primes += item
#             else:
#                 not_primes += item
#     else:
#         print(f'Sum of all prime numbers is: {primes}')
#         print(f'Sum of all non prime numbers is: {not_primes}')
#         break

# from math import sqrt; from itertools import count, islice
# #
# # def isPrime(n):
# #     return n > 1 and all(n%i for i in islice(count(2), int(sqrt(n)-1)))
# #
# # if isPrime(int(input()):
# #     print()


# Zadacha 8
# juri = int(input())
# # raw_grades = 0
# # number_presentations = 0
# # finish = False
# #
# # while not finish:
# #     presentation = input()
# #     score = 0
# #     if presentation != 'Finish':
# #         for i in range(juri):
# #             score += float(input())
# #         raw_grades += score
# #         average_score = score / juri
# #         print(f'{presentation} - {average_score:.2f}.')
# #         number_presentations += 1
# #     else:
# #         print(f"Student's final assessment is {raw_grades / (juri * number_presentations):.2f}.")
# #         finish = True
# #         break


# Zadacha 9

# catch = int(input())
#
# value = 0
# tax = 0
# profit = 0
# fish_count = 0
#
# fish = input()
# weight = float(input())
#
#
# while True:
#     char_sum = 0
#     value = 0
#     fish_count += 1
#     for char in range(len(fish)):
#         char_sum += ord(fish[char])
#     value = char_sum / weight
#     if not fish_count % 3 == 0:
#         tax += value
#     else:
#         profit += value
#     if fish_count == catch:
#         break
#     fish = input()
#     if fish == 'Stop':
#         break
#     weight = float(input())
#
# if fish_count == catch:
#     print(f'Lyubo fulfilled the quota!')
#     if profit > tax:
#         print(f"Lyubo's profit from {fish_count} fishes is {profit - tax:.2f} leva.")
#     else:
#         print(f"Lyubo lost {tax - profit:.2f} leva today.")
# else:
#     if profit > tax:
#         print(f"Lyubo's profit from {fish_count} fishes is {profit - tax:.2f} leva.")
#     else:
#         print(f"Lyubo lost {tax - profit:.2f} leva today.")


# Zadacha 10
# n = int(input())
# l = int(input())

# for first_symb in range(1, n):
#     for second_symb in range(1, n):
#         for third_symb in range(ord('a'), ord('a')+l):
#             for fourth_symb in range(ord('a'), ord('a')+l):
#                 if first_symb > second_symb:
#                     larger = first_symb
#                 else:
#                     larger = second_symb
#                 for fifth_symb in range(larger+1, n+1):
#                     print(f'{first_symb}{second_symb}{chr(third_symb)}{chr(fourth_symb)}{fifth_symb}', end=" ")

# for first_symb in range(1, n):
#     for second_symb in range(1, n):
#         for third_symb in range(ord('a'), ord('a')+l):
#             for fourth_symb in range(ord('a'), ord('a')+l):
#                 for fifth_symb in range(1, n+1):
#                     if fifth_symb > first_symb and fifth_symb > second_symb:
#                         print(f'{first_symb}{second_symb}{chr(third_symb)}{chr(fourth_symb)}{fifth_symb}', end=" ")


# Zadacha 11
# n = int(input())
#
#
#     for integer in range(len(str(number))):
#         if n % ord(integer) == 0:
#             special = True
#         else:
#             special = False
#             continue
#     if special is True:
#         print(number, end = " ")
#

# n = int(input())
#
# for first in range(1, 10):
#     for second in range(1, 10):
#         for third in range(1, 10):
#             for fourth in range(1, 10):
#                 if n % first == 0 and n % second == 0 \
#                         and n % third == 0 and n % fourth == 0:
#                     print(f'{first}{second}{third}{fourth}', end=" ")
# n = int(input())
# a_list = []
#
# for integer in range(1, 10):
#     if n % integer == 0:
#         a_list.append(integer)
#
# for value1 in a_list:
#     for value2 in a_list:
#         for value3 in a_list:
#             for value4 in a_list:
#                 print(f'{value1}{value2}{value3}{value4}', end=" ")

