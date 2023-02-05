# # ---------  CURRYING  --------------
# #  --------  керування   --------------
#
# # змінює підхід до передавання аргументів в нашу функцію
#
# # 1
# def outer(func):
#     def f1(a):
#         #def f2(b='empty'):
#         def f2(b):
#             func(a, b)
#         return f2
#     return f1
#
#
# def my_p(a, b):
#     print(f'a = {a}\nb = {b}')
#
#
# my_p('hello', 'world')
# my_p('hello', 'text')
# my_p('hello', 'people')
#
# print('**************************************')
#
# # !!! --- currying  --- !!!
# x = outer(my_p)('hello')
# x('world')
# x('text')
# x('people')
#
# # !!! --- currying  --- !!!
# outer(my_p)('hello')('world')
#
# #outer(my_p)('hello')()

# ----------------------------------------------------------

# # 2 програма виводить інфо про себе:
# def curry_my_info(func):
#     def f1(name):
#
#         def f2(surname):
#
#             def f3(age):
#                 return func(name, surname, age)
#             return f3
#         return f2
#     return f1
#
#
# def my_info(name, surname, age):
#     return f'name = {name}\tsurname = {surname}\tage = {age}'
#
#
# # x = my_info('n', 's', 12)
# # print(x)
# n, s, a = input(':'), input(':'), input(':')
# print(curry_my_info(my_info)(n)(s)(a))

# ----------------------------------------------------------------

# # 3 повернути результат множення
# def curry_math_m(func):
#     def f1(a):
#         def f2(b):
#             return func(a, b)
#         return f2
#     return f1
#
#
# def math_m(a, b):
#     return a**2 + 2*a*b + b**2
#
#
# print(curry_math_m(math_m)(3)(4))

# -------------------------------------------------------------------------

# # 4 шоб не писати функції currying використовуєм partial
# from functools import partial
#
#
# def math_m(a, b):
#     return a**2 + 2*a*b + b**2
#
#
# x = partial(math_m, a=3, b=4)
# print(x())
# # x = partial(math_m, a=3)
# # print(x(b=4))

# --------------------------------------------------------

# # 5 MAP()
# # Коли для ітерованого алемента потріbно застосувати іншу функцію
#
# # x = list(map(int, input(':').split()))
# y = list(map(lambda x: int(x)+2, input(':').split()))
# #print(x)
# print(y)

# ------------------------------------------------------------------

# # 6
res = list(map(lambda x: x + 'a', 'hello'))
print(res)   # ['ha', 'ea', 'la', 'la', 'oa']

# --------------------------------------------------------------------

# # 7  ---- next()
# res = map(lambda x: x + 'a', 'hello')
# print(next(res))   # ha
# print(next(res))   # ea

# --------------------------------

# # 7  ---- next() + iter()
# res = map(lambda x: x + 'a', 'hello')
# for i in range(5):
#     print(next(res))   # ha
#
# lst = iter([5, 5, 7, 10])
# for i in range(4):
#     print(next(lst))

# ------------------------------------------------

# # 8
# # Користувач вводить дійсні числа в одну стрічку через пробіл.
# # За допомогою функції map перетворити їх в дійсні числа,
# # та відобразити лише перші 2, за умову що буде введено як мінімум 2.
# res = map(float, input(':').split())
# for i in range(2):
#     # print(*list(res))
#     print(next(res))
#
# # ------------------------------------------------------

# # 9
# # Користувач вводить цілі числа в одну стрічку через пробіл
# # (як від'ємні, так і додатні), за допомогою функції map,
# # перетворіть цю стрічку в список цілих чисел по модулю
#
# s = '4 -5 8 -1 -10 3'
#
#
# def a(val):
#     return abs(int(val))
#
#
# print(*list(map(a, s.split())))
# #print(*list(map(lambda val: abs(int(val), s.split()))))

# ---------------------------------------------------------------

# # 10
# # Вводиться стрічка у наступному форматі ключ_1=значеня_1 ключ_2=значеня_
# # 2 ... ключ_N=значеня_N. За допомогою функції map перетворіть її
# # в кортеж наступного формату (('ключ_1', 'значеня_1'),
# # ('ключ_2', 'значеня_2'), ..., ('ключ_N', 'значеня_N'))
# s = 'aaa=123 bbb=321 ccc=456'
# print(tuple(map(lambda val: tuple(val.split('=')), s.split())))
#

# ---------------------------------------

# # 11
# # Вводяться назви міст в одну стрічку через пробіл.
# # Необхідно використати функцію filter, яка повертала
# # б тільки назви довжиною понад 5 символів.
# # Відобразіть лише перші три отримані значення
# # за допомогою функції next і відобразіть їх на екрані
# # в один рядок через пробіл.
# s = 'Lviv Odessa Kyiv Rivne Mykolayiv'
# res = list(filter(lambda text: len(text) > 5, s.split()))
# print(res)


# ---------------------------------------------------------

# 12
# Вводиться список цілих чисел в один рядок через пробіл.
# Необхідно залишити у ньому лише двозначні числа.
# Реалізувати програму за допомогою функції filter.
# Результат відобразити на екрані
# у вигляді послідовності чисел, що залишилися, в один рядок через пробіл.
s = '-3 44 456 22 1 -2'
res = list(filter(lambda num: len(num) == 2 and num[0][0] != '-', s.split()))
print(res)

