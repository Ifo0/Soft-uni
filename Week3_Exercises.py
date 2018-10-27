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

# hours = []
# minutes = []
#
# for x in range(0,23):
#     hours.append(x)
# for x in range(0,60):
#     minutes.append(x)
#
# hour = hours[int(input()]
# # minutes = int(input())

#Zadacha 6
# import math
#
# bro_a = 1 / float(input())
# bro_b = 1 / float(input())
# bro_c = 1 / float(input())
# father = float(input())
#
# cleaning_time = 1 / (bro_a + bro_b + bro_c)
# total_cleaning_time = cleaning_time + (0.15 * cleaning_time)
#
# time_left = father - total_cleaning_time
#
# print(f'Cleaning time: {total_cleaning_time:.2f}')
#
# if time_left > 0:
#     print(f'Yes, there is a surprise - time left -> {math.floor(time_left)} hours.')
# else:
#     print(f"No, there isn't a surprise - shortage of time -> {math.ceil(abs(time_left))} hours.")

#Zadacaha 7
family_income = float(input())
gpa = float(input())
min_salary = float(input())

social = 0.35 * min_salary
excellence = gpa * 25

if family_income < min_salary:
    if gpa < 4.50:
        print('You cannot get a scholarship!')
    elif gpa >= 4.50 and gpa < 5.50:
        print(f'You get a Social scholarship {round(social)} BGN')
    elif gpa >= 5.50:
        if excellence < social:
            print(f'You get a Social scholarship {int(social)} BGN')
        elif excellence >= social:
            print(f'You get a scholarship for excellent results {int(excellence)} BGN')
elif family_income > min_salary:
    if gpa < 5.50:
        print('You cannot get a scholarship!')
    if gpa >= 5.50:
        print(f'You get a scholarship for excellent results {int(excellence)} BGN')
#


#Zadacha 8

import math
# steps = int(input())
# dancers = int(input())
# days_to_learn = int(input())
#
# steps_a_day = steps / days_to_learn / steps
#
# percent_per_dancer = math.ceil(steps_a_day * 100) / dancers
#
# if steps_a_day > 0.13:
#     print(f'No, They will not succeed in that goal! Required {percent_per_dancer:.2f}% steps to be learned per day.')
# else:
#     print(f'Yes, they will succeed in that goal! {percent_per_dancer:.2f}%.')

#Zadacha 9
# import math
# record_sek = float(input())
# distance_meters = float(input())
# sec_per_met = float(input())
#
# time_to_swim = distance_meters * sec_per_met
# fatigue = math.floor(distance_meters / 15) * 12.5
# total_time_to_swim = time_to_swim + fatigue
#
# if total_time_to_swim < record_sek:
#     print(f'Yes, he succeeded! The new world record is {total_time_to_swim:.2f} seconds.')
# else:
#     print(f'No, he failed! He was {(total_time_to_swim - record_sek):.2f} seconds slower.')