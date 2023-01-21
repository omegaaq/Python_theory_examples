#   --------- FUNCTION PART 2 --------------

# # 1
# x = 0
# def outer():
#     x = 1
#     def inner():
#         x = 2
#         print(f' {x}')   #2
#     inner()
#     print(f'{x}')  # 1
#
#
# outer()
# print(f' {x}')  # 0

# #_______________________________________________________________________________
#
# # 2
# x = 22
#
# def func():
#     global x
#     print(x)   # 22
#     x += 1
#     print(x)   # 23
#
# func()

#_______________________________________________________________________________

# # 3
# x = 22
#
# def func():
#
#     print(x)   # 22
#
#
# func()

#-----------------------------------------------------------------------------

# # 4
# x = 22
#
# def func():
#     global x
#     print(x)
#     x = 5
#
#
# func()  # 22
# print(x)    # 5
#
# #_______________________________________________________________________________

# # 5
# def func():
#     global x
#     print(x)
#     x = 5
#
#
# func()
# print(x)      # ERROR
# #----------------------------------------------

# # 6
# x = 0
# def outer():
#     x = 1
#     def inner():
#         print(f' {x}')   #1
#     inner()
#     print(f'{x}')  # 1
#
#
# outer()
# print(f' {x}')  # 0
# #---------------------------------------------

# # 7
# x = 0
# def outer():
#     x = 1
#     def inner():
#         global x
#         x = 3
#         print(f' {x}')   #3
#     inner()
#     print(f'{x}')  # 1
#
#
# outer()
# print(f' {x}')  # 3
# # #---------------------------------------------

# # 8
# x = 0
# def outer():
#     x = 2
#     def inner():
#         global x
#         print(f' {x}')   # 0
#         x = 3
#     inner()
#     print(f'{x}')  # 2
#
#
# outer()
# print(f' {x}')  # 3
# # # #---------------------------------------------

# # 9
# x = 0
#
# def outer():
#     x = 2
#     global x
#     def inner():
#         print(f' {x}')   # error
#
#     inner()
#     print(f'{x}')  # error
#
#
# outer()
# print(f' {x}')  # error
# # # #---------------------------------------------

# # 10
# a = 22
# def outer ():
#     a = 3
#     print(a)
#
# outer() # 3
# print(a) # 22

#-----------------------------

# # 10
# a = 22
# def outer ():
#     global a
#     a = 3
#     print(a)
#
# outer() # 3
# print(a) # 3
#
# #------------------------------------------

# # 11
# x = 0
#
# def outer():
#     x = 1
#     def inner():
#         nonlocal x
#         print(f' {x}')   # 1
#
#     inner()
#     print(f'{x}')  # 1
#
#
# outer()
# print(f' {x}')  # 0
# # #------------------------------------------

# # 12
# x = 0
#
# def outer():
#     x = 1
#     def inner():
#         nonlocal x
#         x = 3
#         print(f' {x}')   # 3
#
#     inner()
#     print(f'{x}')  # 3
#
#
# outer()
# print(f' {x}')  # 0
# # #------------------------------------------

# # 13
# x = 0
#
# def outer():
#     pass
#     def inner():
#         nonlocal x
#         x = 3
#         print(f' {x}')   # error
#
#     inner()
#     print(f'{x}')  # error
#
#
# outer()
# print(f' {x}')  # error
# # #------------------------------------------

# # 14
# x = 0
#
# def outer():
#     global x
#     x = 1
#     def inner():
#         nonlocal x
#         x = 3
#         print(f' {x}')   # error
#
#     inner()
#     print(f'{x}')  # error
#
#
# outer()
# print(f' {x}')  # error
# # #------------------------------------------

# =======================================================================
# ----------------------  РОЗПАКУВАННЯ І ЗАПАКОВУВАННЯ

# # 15
#
# # *x - запаковуємо в
# # **x - запаковуємо в словник
# *x, y = (1, 2, 3, 4)
# print(f'x = {x}\ty={y}')  # x = [1, 2, 3]	y=4
#
# # ------------------------------------------------

# # 16
#
# # *x -
# *x, y = 'hello'
# print(f'x = {x}\ty={y}')  # x = ['h', 'e', 'l', 'l']	y='o'
#
# # ------------------------------------------------

# # 17
# *x = 1, 2 , 3
#
# print(x) # error
# # ------------------------------------------------

# # 18
# a = [1, 2, 3]
# b = (a, )
# c = (*a,)
# print(b)  # ([1, 2, 3],)
# print(c)  # (1, 2, 3)
# # # ------------------------------------------------

# # 19
# a = [1, 2, 3]
# q = [11, 'hello', True]
# b = (a, )
# c = (*a, *q)
# print(b)  # ([1, 2, 3],)
# print(c)  # (1, 2, 3)
# # # ------------------------------------------------

# # 20  розпаковка кортежу
# a = -2, 4
# b = 2, 4
# # print(range(a)) # error
# print(range(*a))  # range(-2, 4)
# print([*range(*a)])  # [-2, -1, 0, 1, 2, 3]
# print(*[*range(*a)])  # -2 -1 0 1 2 3
# # # ------------------------------------------------

# # 21
# # Користувач вводить список із 6 чисел в одну стрічку через пробіл, наприклад
# # 2 13 8 22 186 69, перші 3 цифри потрібно занести в змінну lst, інші в змінну a, b та c.
# # результат виводу print(*lst) має бути 2 13 8.
#
# *lst, a, b, c = [int(x) for x in input('enter num').split()]
# print(*lst)  # 1 2 3
# print(a)     # 4
# print(b)     # 5
# print(c)     # 6
# # ------------------------------------------------

# # 22
#
# # Користувач вводить список дійсних чисел та список слів кожен зберегти
# # в окрему змінну. Необхідно сформувати єдиний список lst який вмістить
# # в собі два попередніх, де перше показати усі слова, а потім числа.
#
# lst_nums = [int(x) for x in input('enter:').split()]
# lst_words = input('enter:').split()
#
# res = [*lst_words, *lst_nums]
# print(res)

# ===========================================================================

# ----------------- FUNCTIONS AND ARGUMENTS ----------------------

# # 23
# def fun(a, b):
#     print(f'a = {a} b = {b}')
#
#
# fun(4, 8)  # a = 4 b = 8
#
# # ----------------------------

# # 24  ---   передача іменованих арументів ------
# def fun(a, b):
#     print(f'a = {a} b = {b}')
#
#
# fun(b=6, a=2)  # a = 2 b = 6
#
# # ----------------------------

# # 25  ---   передача іменованих арументів ------
# def fun(c, a, b):
#     print(f'a = {a} b = {b}')
#     print(c)
#
#
# fun(b=6, a=2, c='hello')  # a = 2 b = 6  hello
#
# # ----------------------------

# # 26  ---   міксована передача іменованих арументів ------
# def fun(c, a, b):
#     print(f'a = {a} b = {b}')
#     print(c)
#
#
# fun(3, a=2, c='hello')  # error

# ----------------------------

# # 27
# def func(name, age):
#     print(age, name)
#
#
# func(name='vlad',14) # error

#---------------------------------------------------

# # 28
# def func(age, name):
#     print(age, name)
#
#
# func(18,name='vlad')
#---------------------------------------------------

# 29 --- ФАКТИЧНІ ТА ФОРМАЛЬНІ ПАРАМЕТРИ

# # name='vlad' це формальний параметр
# # age це фактичний параметр
#
# def func(age, name='vlad'):
#     print(age, name)

# -------------------------------------------------

# # 30
# def func(x, y, operation=False):
#     if operation:
#         return x + y
#     return x - y
#
#
# a = func(10, 2)
# print(a)

#---------------------------------------

# # 31 передати довільну кількість аргументів
# def func(*args):
#     print(args)
#
#
# func('hello',1,True,2)  # ('hello', 1, True, 2)

# ----------------------------------------

# # 32
# # позиційний аргумент запхали в num
# def func(num, *args):
#     print(num)
#     print(args)
#
#
# func('hello',1,True,2)  # hello    (1, True, 2)

# -----------------------------------------------------------

# # 33
#
# def func(num, lst=[]):
#     lst.append(num)
#     return lst
#
#
# x = func(5)
# x = func(6)
# print(x)  # [5, 6]
# print(x)  # [5, 6]

#------------------------------------------

# # 34 перероблений варіант № 33
#
# def func(num, lst=None):
#     if lst is None:
#         lst = []
#     lst.append(num)
#     return lst
#
#
# x = func(10)
# # x = func(10, [12, 3])
# print(x)  # 10
# # print(x)  # [12, 3, 10]

#-----------------------------------------------


# 35
#  ------- ! після **kwargs не можна нічого передавати як аргумент!!!!!
def func(x, *args, **kwargs):
    print(x)
    print(args)
    print(kwargs)


func(13, 'hello', False, name='vlad', age=13, city='lviv')