# ----------------- DEKORATORS ----------------------
# приймає функцію в якості аргумента і повертає нам іншу фунцію
import time


# # variant  1
# def func_decorator(func):
#     def wrapper():
#         print('do begin:')
#         func()
#         print('do after:')
#     return wrapper
#
#
# def my_print():
#     print('func my_print work!')
#
#
# def say_hello():
#     print('hello')
#     print('end of func')
#
#
# my_print = func_decorator(my_print)
# my_print()
#
# say_hello = func_decorator(say_hello)
# say_hello()

# ------------------------------------------------
# # variant 2 with @
# def func_decorator(func):
#     def wrapper():
#         print('do begin:')
#         func()
#         print('do after:')
#     return wrapper
#
#
# @func_decorator
# def my_print():
#     print('func my_print work!')
#
#
# @func_decorator
# def say_hello():
#     print('hello')
#     print('end of func')
#
#
# my_print()
# say_hello()

# -------------------------------------------------------

# # 3 with arguments, *args = this is tuple
# def func_decorator(func):
#     def wrapper(*args):
#         print('do begin:')
#         func(*args)
#         print('do after:')
#     return wrapper
#
#
# @func_decorator
# def my_print(text, a, b):
#     print(f'this is yor text =  {text} and {a}! and {b}')
#
#
# my_print('hey', 'abc', 3.14)

# ----------------------------------------------------------
# # 4 this is DECORATOR!
# def func_decorator(func):
#     def wrapper(*args, **kwargs):
#         print('do begin:')
#         res = func(*args)
#         print('do after:')
#         return res
#     return wrapper
#
#
# @func_decorator
# def my_print(text, a, b):
#     print(f'this is yor text =  {text} and {a}! and {b}')
#     return 'new text : ' + text
#
#
# print(my_print('hey', 'abc', 3.14))
#
# # # Result:
# # do begin:
# # this is yor text =  hey and abc! and 3.14
# # do after:
# # new text : hey
# -----------------------------------------------------

# # 5
# def func_dec(func):
#     def wrapper(*args):
#         start = time.time()
#         func(*args)
#         end = time.time()
#         return f'function time = {end - start} seconds.'
#     return wrapper
#
#
# @func_dec
# def abc(count):
#     i = 0
#     while i < count:
#         print(i)
#         i += 1
#
#
# print(abc(100))
# -------------------------------------------------------------------

# # 6
# # Створіть функцію з назвою get_rec_square, яка вираховує площу
# # прямокутника за параметром width та height.
# # Вона повертає лише результат. Створіть декоратор, який буде показувати результа
# # т у вигляді стрічки "Rectangle square = *value*".
# def dec(func):
#     def wrap(*args):
#         res = func(*args)
#         print(f'rectangle square = {res}')
#         #print(f'rectangle square = {func(*args)}')
#     return wrap
#
#
# @dec
# def get_rectangle_square(width, height):
#     return width * height


# get_rectangle_square(2, 3)
# --------------------------------------------------------------------------
# # 7
# # Створити функцію, яка приймає перелік продуктів в одну стрічку через пробіл,
# # ця функція перетворює цю стрічку у список продуктів, та повертає його.
# # Створіть декоратор, який виведе перелік продуктів у форматі:
# # 1. назва
# # 2. назва_2
# def dec(func):
#     def wrapper(* args):
#         for num, val in enumerate(func(*args), 1):
#             print(f'{num}. {val}')
#
#     return wrapper
#
#
# @dec
# def slice_text(text):
#     return text.split()
#
#
# products = input('enter products:')
# slice_text(products)

# ------------------------------------------------------
# # 8
# # Користувач вписує числа в одну стрічки через пробіл, створіть функцію
# # convert_to_list, яка буде приймати цю стрічку та повертати список чисел.
# # Використовуючи декоратор, відсортуйте ці числа по зростанню, та відобразіть їх.
# def sort_num_list(func):
#     def wrapper(*args):
#         print(sorted(func(*args)))
#     return wrapper
#
#
# @sort_num_list
# def convert_to_list(s):
#     return [int(value) for value in s.split()]
#
#
# convert_to_list(input('enter:'))

# ---------------------------------------------------------

# 9
# -----------      ОПИС ФУНКЦІЇ    -------------
# def abc():
#     """ this is function description"""
#     print('hello')
#
#
# print(abc.__doc__)   # this is function description
# print(abc.__name__)  # abc

# -------------------------------------
# # 10
# from functools import wraps
#
#
# def sort_num_list(func):
#     @wraps(func)
#     def wrapper(*args):
#         print(sorted(func(*args)))
#     return wrapper
#
#
# @sort_num_list
# def convert_to_list(s):
#     """ this is some description"""
#     return [int(value) for value in s.split()]
#
#
# convert_to_list(input('enter:'))
# print(convert_to_list.__doc__)  # this is some description
# print(convert_to_list.__name__) # convert_to_list

# --------------------------------------------------------

# # 11
# def dec(new_text):
#     def wrapper(func):
#         def inside(*args):
#             print(f'{new_text} {func(*args)}')
#         return inside
#     return wrapper
#
#
# @dec(new_text='its some new text')
# def abc(text):
#     return text
#
#
# abc(input('enter:'))
#
# # -----------------------------------------------

# # 12
# # Вводиться стрічки цілих чисел через пробіл, функція перетворює цю стрічку
# # у список чисел, та повертає їхню суму.
# # Створити декоратор з одним параметром name, його використовуємо для
# # формування стрічки "{name} = {сума_чисел}, поверніть її, відобразіть її.
# def dec(name='some text'):
#     def wrapper(func):
#         def inside(*args):
#             res = func(*args)
#             print(f'name = {name}\nsum = {res}')
#         return inside
#     return wrapper
#
#
# @dec('its a some text')
# def sum_of_list_numbers(s):
#     return sum([int(v) for v in s.split()])
#
#
# sum_of_list_numbers(input('enter:'))

#-----------------------------------------------------------------

# # 13
# def dec(name='some text'):
#     def wrapper(func):
#         def inside(*args):
#             res = func(*args)
#             print(f'name = {name}\nsum = {res}')
#         return inside
#     return wrapper
#
#
# @dec(input('abc:'))
# def sum_of_list_numbers(s):
#     return sum([int(v) for v in s.split()])
#
#
# @dec(input('ccc:'))
# def sum_of_2():
#     return 4 + 4
#
# sum_of_list_numbers(input('enter:'))
# sum_of_2()