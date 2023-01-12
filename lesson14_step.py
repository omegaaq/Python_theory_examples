# #  FUNCTION

# # 1 оголошення функціїї
# def func():
#     print('A')
#     print('B')
#     print('C')
# #--------------------------------------------------------
#
# # 2 виклик фунції
# func()
#-------------------------------------------------------------------

# # 3 Створити функцію без параметрів, яка зчитує число,
# це число це номер місяця,
# показати скільки днів у даному місяці
# та назву місяця у письмовій формі.

# import calendar
#
#
# def get_month_info(data):
#     if data.isdigit() and 1<= int(data)<=12:
#         print(f'In {calendar.month_name[int(data)]} we got {calendar.monthrange(2023,9)[1]} days.')
#     else:
#         print('error')
#
# num = input('enter month from 0 to 12')
# get_month_info(num)
# #---------------------------------------------------------------------

# # 4 ====PARAM VE ARGUMENTS
# # name ===== this is param
# # 'vlad' ==== this is argument
# def say_hello(hello,age):
#     print(f'Hello dear {hello} age is {}')
# say_hello('vlad', 13)
# # -----------------------------------------------

# # 5 Функція має один параметр, після оголошення функції введіть вагу,
# та викличте функцію з цим аргументом.
# Результат виводу -> “Вага товару 32.12 кг.”

# def show_weight(weight,name):
#     print(f'weight of good {name} = {weight} kg')
#
# show_weight(float(input('enter weight:')),'Apple')
#
# #-------------------------------------

# # 6  Створити функцію, яка приймає список чисел,
# та відображає мінімальне, максимальне та суму усіх чисел.
# Числа користувач вводить через пробіл
# Результат відобразити у форматі
# MIN = ?
# MAX = ?
# SUM = ?

# def max_min_sum(lst_num):
#     print(f'min = {min(lst_num)}\nmax = {max(lst_num)}\nsum = {sum(lst_num)}')
#
#
# max_min_sum([int(value) for value in input('enter:').split()])
# #-----------------------------------------

# # 7 Функція приймає два числа, це ширина та висота прямокутника,
# # обрахуйте периметр та відобразіть користувачу результат у форматі
# # “Периметр прямокутника зі сторонами ? та ? = результат”.
# def p_rectangle(width, height):
#     print(f'perimetr of rectangle with sides {width} x {height} = {(width + height) * 2}')
#
#
# p_rectangle(int(input('width:')), int(input('height:')))
# # -----------------------------------------------------------

#  ------------------------ Function return result------------------------
# # 8
# def edit(text, spec_symb):
#     if text:
#         return spec_symb + text + spec_symb
#     return 'error'
#
#
# x = edit('hi all', ' * ')
# print(x)
# # --------------------------------------

# # 9 піднести число до степені
# def best_read(res):
#     print(res)
#
# def stepin(num, power):
#     return num ** power
#
#
# x = stepin(2, 2)
# # print(x)
# best_read(x)
# -------------------------------------------

# # 10 передаємо в функці. 2 числа повернути менше з них
# def min_max(x, y):
#     return x if x < y else y
#
#
# x = int(input('x: '))
# y = int(input('y: '))
# res = min_max(x, y)
# print(res)
# #------------------------------------------------














