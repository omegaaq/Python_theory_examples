# # ---    Z I P   -----------------
#         -------
# # 1
# a = [1, 2, 3, 4]
# b = [5, 6]
# c = list(zip(a, b))
# print(c)  # [(1, 5), (2, 6)]

# ---------------------------------------------------
# # 2
# lst_names = ['vira', 'oleg', 'vlad']
# lst_phones = ['123', '234', '345']
# lst_ages = [13, 20, 30]
# c = tuple(zip(lst_names, lst_phones, lst_ages))
# print(c)

# ----------------------------------------------

# # 3
# lst_names = ['vira', 'oleg', 'vlad']
# lst_phones = ['123', '234', '345']
# lst_ages = [13, 20, 30]
# c = tuple(zip(lst_names, lst_phones, lst_ages))
# for tup in c:
#     print(tup)    #  ('vira', '123', 13)
#                   #  ('oleg', '234', 20)
#                   #   ('vlad', '345', 30)


# -------------------------------------------------------

# 4 перемножити між собою числа з двох кортежів
# a = [1, 2, 3, 4, 9]
# b = [5, 6, 2, 2]
# res = list(map(lambda tup: tup[0]*tup[1], zip(a, b)))
# print(res)

# --------------------------------------------------

# 5
# a = [1, 2, 3, 4]
# b = [6, 7, 8, 5, 7]
# c = [10, 11, 15, 22]
# d = [5, 10, 13]
# res = tuple(zip(a, b, c, d))
# # print(*res)
# for v in zip(*res):
#     print(*v)
#
# #транспанована матриця
# for v in res:
#     print(*v)

# ------------------------------------------------------------------

# # -------Reduce
# перебере кожен з елементів і зробить з нтмт те що іказано в функції-------
# # 6
# from functools import reduce
#
# def mnoz(x, y):
#     return x * y
#
# def dod(x, y):
#     return x + y
#
#
# res = reduce(mnoz, (2, 5, 2, 3))
# res2 = reduce(dod, (2, 5, 2, 3))
# print(res)
# print(res2)
#
# res_1 = reduce(lambda a, b: a*b, [2, 3, 4])
# print(res_1)

# --------------------------------------------
# 7 variant 1
from functools import reduce
#
#
res = reduce(lambda a, b: a + ' ' +b, input(':').split())
print(res)

# --------------------------------------------

# # 8 variant 2
# from functools import reduce
#
#
# text = input().split()
# print(text)
# def union(a, b):
#     return a + ' ' + b
#
#
# res = reduce(union, text)
# print(res)

# ------------------------

# # 9 variant 3
# from functools import reduce
# text = input().split()
# print(text)
# res = ''
# for val in text:
#     res += val
# print(res)

# -----------------------------------------------------
# # 10
# from functools import reduce
#
# print(reduce(lambda x, y: x * y, range(1, int(input()) + 1)))

# -------------------------------------------------------------

# 11
# гра 'Словко'

# from random import choice
# lst_guess_words = ['океан', 'вітер', 'потяг', 'кумис', 'файно', 'броди']

# def check_word_decorator(func):
#     used_words = []
#     def wrapper(*args, **kwargs):
#         print(kwargs)
#         print(func(*args, **kwargs))
#         #pass
#     return wrapper
#
#
# @check_word_decorator
# def check_word(guess, answer):
#     if guess == answer:
#         return True
#     return False


# lives = 6
#
# while lives > 0:
#     rand_word = choice(lst_guess_words)
#     print(rand_word)
#     user_answer = input('enter word:')
#     res = check_word(guess=rand_word, answer=user_answer)
#



