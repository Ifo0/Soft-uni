# Zadacha 1
# time_a = int(input())
# time_b = int(input())
# time_c = int(input())
#
# total_time = time_a + time_b + time_c
#
# if total_time < 60:
#     print('0:' + f'{total_time}'.zfill(2))
# elif total_time >= 60 and total_time < 120:
#     print('1:' + f'{total_time % 60}'.zfill(2))
# else:
#     print('2:' + f'{total_time % 120}'.zfill(2))

# Zadacha 2
# num = int(input())
#
# bonus = 0
# if num < 101:
#     bonus += 5
# elif num > 100 and num < 1001:
#     bonus += 0.2 * num
# else:
#     bonus += 0.1 * num
#
# if num % 2 == 0:
#     bonus += 1
# elif num % 5 == 0:
#     bonus += 2

# print(bonus)
# print(num + bonus)

#Zadacha 3
# speed = float(input())
#
# if speed <= 10:
#     print('slow')
# elif speed > 10 and speed <= 50:
#     print('average')
# elif speed > 50 and speed <= 150:
#     print('fast')
# elif speed > 150 and speed <= 1000:
#     print('ultra fast')
# else:
#     print('extremely fast')


#Zadacha 4
# measure = float(input())
# input_unit = input()
# output_unit = input()
# if input_unit == 'in':
#     input_unit = 'inc'
# if output_unit == 'in':
#     output_unit = 'inc'
#
# m = 1
# mm = 1000
# cm = 100
# mi = 0.000621371192
# inc = 39.3700787
# km = 0.001
# ft = 3.2808399
# yd = 1.0936133
#
# output = measure / eval(input_unit) * eval(output_unit)
# print(f'{output:.8f}')

#Zadacha 5
# hour = int(input())
# minutes = int(input())
#
#
# if minutes < 45:
#     print(f'{hour}' + ':' + f'{minutes+15}'.zfill(2))
# elif hour == 23 and minutes >= 45:
#     print('0:' + f'{(minutes+15) % 60}'.zfill(2))
# else:
#     print(f'{hour+1}:' + f'{(minutes+15) % 60}'.zfill(2))

hours = []
minutes = []

for x in range(0,23):
    hours.append(x)
for x in range(0,60):
    minutes.append(x)

hour = int(input())
minutes = int(input())

