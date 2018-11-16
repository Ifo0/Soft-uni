# Zadacha 1

# for i in range(7, 1000, 10):
#     print(i)

# Zadacha 2
# n = int(input())
# # sumi = 0
# # maxi = 0
# #
# # for i in range(n):
# #     get = int(input())
# #     sumi += get
# #     if maxi < get:
# #         maxi = get
# #
# # sumi -= maxi
# # if sumi == maxi:
# #     print(f'Yes')
# #     print(f'Sum = {maxi}')
# # else:
# #     print('No')
# #     print(f'Diff = {abs(maxi - sumi)}')

# Zadacha 3
import sys
# n = int(input())
# odd_sum =  even_sum = 0
# odd_min = odd_max = even_min =even_max = 'No'
# odd = False
# even = False
#
# odd_bootstrap = 0
# even_bootstrap = 0
#
# for i in range(1, n + 1):
#     get = float(input())
#     if i % 2 == 0:
#         even_sum += get
#         if even_bootstrap == 0:
#             even_min = get
#             even_max = get
#             even_bootstrap += 1
#         if get > even_max:
#             even_max = get
#         if get < even_min:
#             even_min = get
#     else:
#         odd_sum += get
#         if odd_bootstrap == 0:
#             odd_min = get
#             odd_max = get
#             odd_bootstrap += 1
#         if get > odd_max:
#             odd_max = get
#         if get < odd_min:
#             odd_min = get
#
# if odd_min == 'No':
#     print(f'OddSum={odd_sum:}')
#     print(f'OddMin={odd_min}')
#     print(f'OddMax={odd_max}')
# else:
#     print(f'OddSum={odd_sum:}'.rstrip('0').rstrip('.'))
#     print(f'OddMin={odd_min}'.rstrip('0').rstrip('.'))
#     print(f'OddMax={odd_max}'.rstrip('0').rstrip('.'))
#
# if even_min == 'No':
#     print(f'EvenSum={even_sum}')
#     print(f'EvenMin={even_min}')
#     print(f'EvenMax={even_max}')
# else:
#     print(f'EvenSum={even_sum}'.rstrip('0').rstrip('.'))
#     print(f'EvenMin={even_min}'.rstrip('0').rstrip('.'))
#     print(f'EvenMax={even_max}'.rstrip('0').rstrip('.'))
#

# Zadacha 4
# n = int(input())
# difference = 0
# old_sum = 0
# max_difference = 0
# bootstrap = 0
#
# for i in range(n):
#     first = int(input())
#     second = int(input())
#     sum_num = first + second
#     if bootstrap == 0:
#         difference == 0
#         bootstrap += 1
#     else:
#         difference = abs(sum_num - old_sum)
#         if difference > max_difference:
#             max_difference = difference
#     old_sum = sum_num
#
# if difference == 0:
#     print(f'Yes, value={sum_num}')
# else:
#     print(f'No, maxdiff={max_difference}')


# Zadacha 5
# n = int(input())
# less200 = less400 = less600 = less800 = above = 0
# all_num = 0
#
# for i in range(n):
#     number = int(input())
#     if number < 200:
#         less200 += 1
#     elif 200 <= number < 400:
#         less400 += 1
#     elif 400 <= number < 600:
#         less600 += 1
#     elif 600 <= number < 800:
#         less800 += 1
#     elif number >= 800:
#         above += 1
#     all_num += 1
#
# print(f'{(less200 / all_num) * 100:.2f}%')
# print(f'{(less400 / all_num) * 100:.2f}%')
# print(f'{(less600 / all_num) * 100:.2f}%')
# print(f'{(less800 / all_num) * 100:.2f}%')
# print(f'{(above / all_num) * 100:.2f}%')


# Zadacha 6

# n = int(input())
# mod2 = mod3 = mod4 = 0
# all_mod = 0
#
# for i in range(n):
#     number = int(input())
#     if number % 2 == 0:
#         mod2 += 1
#     if number % 3 == 0:
#         mod3 += 1
#     if number % 4 == 0:
#         mod4 += 1
#     all_mod += 1
#
# print(f'{(mod2 / all_mod) * 100:.2f}%')
# print(f'{(mod3 / all_mod) * 100:.2f}%')
# print(f'{(mod4 / all_mod) * 100:.2f}%')


# Zadacha 7
# tabs = int(input())
# salary = float(input())
#
# for i in range(tabs):
#     website = input()
#     if website == 'Facebook':
#         salary -= 150
#     elif website == 'Instagram':
#         salary -= 100
#     elif website == 'Reddit':
#         salary -= 50
#     if salary <= 0:
#         print('You have lost your salary.')
#         break
#
# if salary > 0:
#     print(f'{salary:.0f}')




