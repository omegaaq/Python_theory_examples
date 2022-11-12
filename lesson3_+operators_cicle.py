# # Операции сравнения
# print("1 == 1:", 1 == 1)
# print("1 == 2:", 1 == 2)
# print("1 != 1:", 1 != 1)
# print("1 != 2:", 1 != 2)
# print("1 > 1:", 1 > 1)
# print("1 > 2:", 1 > 2)
# print("2 > 1:", 2 > 1)
# print("1 < 1:", 1 < 1)
# print("1 < 2:", 1 < 2)
# print("2 < 1:", 2 < 1)8
#
# print("1 >= 1:", 1 >= 1)
# print("1 >= 2:", 1 >= 2)
# print("2 >= 1:", 2 >= 1)
# print("1 <= 1:", 1 <= 1)
# print("1 <= 2:", 1 <= 2)
# print("2 <= 1:", 2 <= 1)
#
#
# # Использование значений в качестве условий
# print(bool(""))
# print(bool(0.0))
# print(bool(None))
# print(bool("IT Step Academy"))
# print(bool(1))
#
#
# # Логические операции
# # ---OPERATOR --- AND
# #true
# competent = True
# responsible = True
# print(competent and responsible)
#
# #false
# competent = True
# responsible = False
# print(competent and responsible)
#
# # ---OPERATOR --- OR
# #true
# competent = True
# responsible = False
# print(competent or responsible)
#
# #false
# competent = False
# responsible = False
# print(competent or responsible)
#
# # ---OPERATOR --- NOT
# #false
# previously_fired = True
# print(not previously_fired)
#
# #true
# previously_fired = False
# print(not previously_fired)

# #exersise
# time = int(input("Enter the current time in hours: ")) % 24
# ticket = False
# money = True
# luggage = False
# #print(money or ticket and not luggage and time > 6)   #true
# print((money or ticket) and not luggage and time > 6)  #false

#-------if------
# #1
# car_speed = 100
# if car_speed > 50:
#  print("Car is faster than 50 km/h")

# #2
# passenger_weight = 400
# if passenger_weight < 300:
#  print("The elevator can go")
#
# #3
# car_speed = 100
# if car_speed > 50 and car_speed < 150:
#     #if 50 < car_speed < 150:
#  print("Car speed is between 50 km/h and 150 km/h")
#

# #4
# year = 2000
# if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
#  print("Year", year, "is leap")

# year = 2000 % 4
# print(year)
# 0

# # ---Cycles
# while condition:
#  print("Cycles")

# # ------  обработке исключений;----
# try:
#  print("Some code")
# except:
#  print("Error processing")
# finally:
#  print("Handling Exceptions")

# # функциях;
# def function():
#  print("Functions")

# #классах.
# class Class:
#  def __init__(self):
#  print("Classes")

# # Операторы ветвления if … else
# #1
# car_speed = 100
# motorcycle_speed = 150
# if car_speed > motorcycle_speed:
#  print("Car is faster than motorcycle")
# if motorcycle_speed > car_speed:
#  print("Motorcycle is faster than car")
# else:
#  print("Car and motorcycle are equally fast")

# #2
# car_speed = 130
# motorcycle_speed = 100
# if car_speed > motorcycle_speed:
#  print("Car is faster than motorcycle")
#  motorcycle_speed += 50
# if motorcycle_speed > car_speed:
#  print("Motorcycle is faster than car")
#  motorcycle_speed += 50
# else:
#  print("Car and motorcycle are equally fast")
#  motorcycle_speed += 50

#  #3
# flowers_amount = 3
# if flowers_amount > 2:
#      print("You have at least 3 flowers")
#      if flowers_amount < 5:
#          print("You have less than 5 flower")

# #4
# number = int(input("Enter the answer number: "))
# if number == 1:
#  print("You’ve chosen answer A")
# else:
#  if number == 2:
#   print("You’ve chosen answer B")
#  else:
#    if number == 3:
#     print("You’ve chosen answer C")
#    else:
#     if number == 4:
#      print("You’ve chosen answer D")
#     else:
#      print("There is no such answer.")

# #5
# account = int(input("Enter how much you put: "))
# account = abs(account)
# if account > 0:
#  withdrawal = int(input("Enter how much you take: "))
#  withdrawal = abs(withdrawal)
#  if withdrawal < account:
#     account -= withdrawal
#     print("Here are your", withdrawal, ".")
#     print("There are", account, "left.")
#   else:
#     print("There are only", account, ".")
# else:
#  print("There are no money in piggy bank")

# # функцию abs(), положительное число
# account = int(input("Enter how much you put: "))
# account = abs(account)
# #account2 = account * -1
# print(account)

# # Типы исключений
# ■ BaseException — базовый тип, из которого происходят
# все остальные, в том числе системные:
# • Exception — базовый тип для «стандартных» и пользовательских исключений:
# ▫ ArithmeticError — арифметическая ошибка:
# ▫ OverflowError  — возникает, когда результат
# арифметической операции слишком велик для
# представления
# • ZeroDivisionError — деление на ноль.
# ■ ImportError — импортировать модуль или его атрибут
# не удалось;
# ■ LookupError — некорректный индекс или ключ:
# • IndexError — индекс не входит в диапазон элементов;
# • KeyError  — несуществующий ключ (например,
# в словаре).
# ■ NameError — не найдено переменной с указанным
# именем;
# ■ RuntimeError — возникает, когда исключение не попадает ни под одну из других категорий;
# ■ SyntaxError — синтаксическая ошибка:
# • IndentationError — неправильные отступы:
# ▫ TabError  — смешивание в  отступах табуляции
# и пробелов
# ■ TypeError — операция применена к объекту несоответствующего типа;
# ■ ValueError — функция получает аргумент правильного
# типа, но некорректного значения

#Перехват исключений
##1 ----try … except
# try:
#  amount = int(input("Enter the amount of received items: "))
#  items_type = input("Specify the type of received items: ")
# except:
#  print("Amount should be an integer")

# #2
# try:
#  amount = int(input("Enter the amount of received items: "))
#  items_type = input("Specify the type of received items: ")
#  parts_number = int(input("Enter the number of parts: "))
#  parts_amount = amount / parts_number
#  print("Supply of", amount, items_type, "saved")
#  print("Each of", parts_number, "parts consists of", parts_amount, items_type)
# except ValueError:
#  print("Amount should be an integer")
# except ZeroDivisionError:
#  print("You cannot divide the delivery into 0 parts")
#

