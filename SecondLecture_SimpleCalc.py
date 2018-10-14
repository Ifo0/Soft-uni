# name = input()
# age = int(input())
#
# print(f'Hello! You are {name} you are {age} years old!')

#Inc to sm
# inches = float(input('Enter value in inches: '))
# constant = 2.54

# print(f"Value in centimeters is {inches*constant}")


#Greeting by name

# name = input()
# print("Hello", name)

#concatenating data
# firstname = input('Your name, please:')
# lastname = input('Your familyname is: ')
# age = input('Enter age: ')
# town = input("Where are you from: ")
#
# print(f'You are {firstname} {lastname}, a {age}-years old person from {town}.')

# a = float(input())
# b = float(input())
# h = float(input())
#
# output = (a + b) * h /2
# print(output)

# import math
#
# r = float(input("What is the radius of the circle: "))
#
# area = math.pi * r * r
# perimeter = 2 * math.pi * r
#
# print(f'The area is {area} and the perimeter is {perimeter}')

# a = float(input())
# h = float(input())
#
# area = a * h / 2
#
# print(f"{area:.2f}")


# celsius = float(input())
#
# farenheit = celsius * 1.8 + 32
#
# print(farenheit)

# import math
#
# radians = float(input())
# degrees = radians * 180 /math.pi
# print(degrees)
#
# #to cut
# cut = math.trunc(degrees)
# math.ceil(degrees)
# math.floor(degrees)


#Exam exercise

length = int(input())
width = int(input())
height = int(input())
percent = float(input())

volume_centimeters = length * width * height
volume_decimeters = volume_centimeters * 0.001
converted_percent = percent * 0.01
volume_needed = volume_decimeters * (1 - converted_percent)
print(f'{volume_needed:.3f}')

# def simple_prog(number):
#     number = int(input('number'))
#     output  = number * 5
#     print(output)
#     return output
#
# def main():
#     simple_prog(sys.argv[0])
#
# if __name__ == '__main__':
#     main()


