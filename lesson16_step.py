# -----  LAMBDA FUNCTION ---------

# lambda function це aнонімна функція може використовуватися будь де в коді повертає результат
# return і прсвоєння в lambda func  робити не можна!

# # 1
# # a, b це аргументи лямбди
# x = lambda a, b: a + b
# print(x(2, 8))
#
# ---------------------------------------
# # 2
# if lambda: 3 + 6 < 15:
#     print('work')
# ----------------------------------------------------
# # 3
# a = [lambda: print(input('enter num:')), lambda: print('i m a lambda func')]
# # a[0]()
# # a[1]()
#
# for value in a:
#     value()

# ----------------------------------------------

# # 4
# lst=None шоб при створенні список був пустий

# def get_filtered(data, filter, lst=None):
#     if lst is None:
#         lst = []
#     for value in data:
#         if filter(value):
#             lst.append(value)
#     return lst
#
#
# a = [3, 8, -2, 6, 10, -1]
# x = get_filtered(a, lambda number: number % 2 == 0)
# y = get_filtered(a, lambda number: number > 5)
# a = get_filtered(a, lambda number: 5 < number < 10)
# print(x)
# print(y)

# -------------------------------------------------------------------


# # 5 Оголосіть анонімну функцію з одним параметром яка буде підносити число до квадрату.
# # # variant 1:
# # x = lambda a: a**2
# # print(x(3))
#
# # variant 2:
# x = lambda num, pow: num**pow
# print(x(15, 3))

# ------------------------------------------------------------------------

# # 6 Оголосіть анонімну функцію з двома параметрами, в якій необхідно повернути
# # результат від ділення x на y, якщо y не ноль, в іншому випадку повертати None.
#
# # l = lambda x, y: x / y if y != 0 else None
# k = lambda x, y: x / y if y else None
# print(k(3,5))

# -------------------------------------------------

# # 7 Оголосіть анонімну функцію з двома параметрами фактичним і формальним,
# # фактичний для дійсного числа, формальний для цілого, який буде вказувати
# # на к-сть знаків після коми (по замовчуванню = 1). Відобразити це форматоване число.
#
# l = lambda num, x=1: round(num, x)
# print(l(3.2345))

# -----------------------------

# # 8 Оголосіть анонімну функцію, яка буде приймати стрічку і повертати True
# # якщо в цій стрічці присутній фрагмент стрічки ‘or’, в іншому випадку False.
# l = lambda text, fragment: True if fragment in text else False
# print(l('asweroraaa', 'or'))

# -------------------------------------------------------

# # # -----------         RECURSIA           ------------------------
# по замовчуванню має обмежену кількість виконань
# це фунція яка викликає сама себе

# # 1
# def rec():
#     print(1)
#     rec()
#
#
# rec()
#
# # ------------------------------------------------------

# # 2  Користувач вводить число, вивести всі числа від 1 до числа користувача включно.
# def rec(num):
#     print(num)
#     if num < 10:
#         rec(num + 1)  # 1 2 3 4 5 6 7 8 9 10
#     print(num)        # 10 9 8 7 6 5 4 3 2 1
#
#
# rec(1)

# ------------------------------------------------------

# # 3 Нарізати число на окремі числа, та показати
# # їх (псс, використовуйте ділення по модулю, остачу від ділення ;) )
#
# # print(543//10)  # 54
# # print(543 % 10) # 3
#
# def rec(num):
#     if num >= 10:
#         rec(num // 10)
#     print(num % 10)   # 4   6   1
#
#
# rec(461)

# --------------------------------------------------------------------

# # 4 порахувати суму всіх чисел
# def slice_m(num):
#     if num <= 10:
#         return num
#     return num % 10 + slice_m(num // 10)
#
#
# x = slice_m(456)
# print(x)

# ------------------------------------------------------------------
#
# # 5 факторіал числа
# def rec(num):
#     if num == 1:
#         return num
#     return rec(num - 1) * num
#
# x = rec(5)
# print(x)