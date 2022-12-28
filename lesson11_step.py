# # # #  гра хрестики нолики
# # -1 empty   -
# # 0 this is  o
# # 1 this is  x
# lst_field=[]
# turn = True
# for _ in range(3):
#     lst_field.append([-1, -1, -1])
# print(lst_field)
#
# while True:
#     for i in range(3):
#         for j in range(3):
#             if lst_field[i][j] == -1:
#                 print('-', end='  ')
#             elif lst_field[i][j] == 0:
#                 print('o', end='  ')
#             else:
#                 print('x', end='  ')
#         print()
#     choice = input('Enter row and col:').split()
#     print(choice)
#
#     # ---- validation ----перевірки-----
#     if len(choice) == 2:
#         for value in choice:
#             if not(value.isdigit()) or int(value) not in range(3):
#                 print('\n\t invalid data \n')
#                 break
#         else:
#             # make move
#             # -1 це пустота
#             if lst_field[int(choice[0])][int(choice[1])] == -1:
#                 lst_field[int(choice[0])][int(choice[1])] = turn
#                 turn = not turn
#
#                 # check win row and col
#                 for i in range(3):
#                     if lst_field[i][0] == lst_field[i][1] == lst_field[i][2] and lst_field[i][2] != -1:
#                         print('work row')
#                         break
#                     elif lst_field[0][i] == lst_field[1][i] == lst_field[2][i] and lst_field[2][i] != -1:
#                         print('work col')
#                         break
#                 # check win diagonal
#                     else:
#                         if lst_field[0][0] == lst_field[1][1] == lst_field[2][2] or \
#                                 lst_field[0][2] == lst_field[1][1] == lst_field[2][0] and \
#                                 lst_field[1][1] != -1:
#                             print('work diagonal')
#                             break
#             else:
#                 print('\n\t this cell is used')
#     else:
#         print('enter 2 values!')
#
# # howework : - > нічия
# #-----------------------------------------------------------------------------------------

# ##  -- К О Р Т Е Ж І----
# використ коли не можна міняти якісь дані
# В КОРТЕЖІ ЕЛЕМЕНТИ НЕ МОЖНА ЗМІНЮВАТИ
# # 1
# a = [1,2,3]
# b = (1, 2, 3)
# print(a.__sizeof__()) # 72
# print(b.__sizeof__()) # 48
# print(b[2])  # 3
# print(b[-1]) # 3
# a[0] = 5  # 5 2 3
# # b[0] = 5 ## not work!
# # ------------------------------------------------------

#  # 2  Оголосити кортеж
# c = 2, 5, 8, 10
# print(c)
# b = (1, 2, 3)
# print(b)
# d = ()
# print(d)
# e = (1, )
# print(e)
# a = tuple()  # # це пустий кортеж
# -------------------------------

# # 3 копіювання кортежів
# # копіємо ссилку
# e = d
# print(id(d))
# print(id(e))
#----------------------------------

# # 4 повноційна копія
# e = tuple(d)
# print(id(d))
# print(id(e))
#---------------------------------

# # 5 зєднуємо кортежі
# a = (1, )
# b = (3, 8, 11)
# c = a + b
# print(c)
# # ----------------------

# # 6 дізнатися індекс кортежу
# a = (1, )
# b = (3, 8, 11)
# c = a + b
# print(c)  # 1 3 8 11
# if 8 in c:
#     print(c.index(8))  # 2
#
# # 7 count
# print(c.count(8))  # 1
#
# # 8 шукати в конкретному діапазоні:
# if 1 in c:
#     print(c.index(1, 0))  # 1 це сисло яке шукаємо, 0 це від якого діапазона
#     print(c.index(8, 1))
#----------------------------------------

# # Особливості кортежів
# a = (True, False, 14, 'Hello', [14, 25, 22, 'Tik'])
# print(id(a[4]))
# a[4][0] = 777
# print(a)  # its work! (True, False, 14, 'Hello', [777, 25, 22, 'Tik'])
# print(id(a[4]))
#
# a += ('qwerty', )
# print(a)
#---------------------------------------

# # cycle in kortej
# for value in a:
#     print(value)
#----------------------------

# # ---- enumerate
# # 1
# for value in enumerate(a, 8): # 8 це другий аргумент з якого буде йти індексація
#     print(value)

# # 2
# for i, value in enumerate(a, 8): # 8 i зберігає індекс а value  значення
#     print(value, i)

# # 3
# # 1
# # 2789693021856
# # 2
# # 2789698014080
# # 3
# # 2789698014912
# # ('1', '2', '3')
# a = tuple()
# for _ in range(3):
#     a += (input(),)
#     print(id(a))
# print(a)
# print(a.__sizeof__())  # 48
#
#
# b = list()
# for _ in range(3):
#     b.append(input())
#     print(id(b))
# print(b)
# print(b.__sizeof__())  # 72
# # 1
# # 2789693158464
# # 2
# # 2789693158464
# # 3
# # 2789693158464
# # ['1', '2', '3']
#---------------------------------------------------------

# # користувач вводить числа через пробіл
# # ці числа требв добавити вже в існуючий заповнений кортеж
# a = (1, True, [7, 8], 'hello')
# a += tuple(input('enter num:').split())
# # числа згенеруються стрічкою
# # enter num:3 4 5
# # (1, True, [7, 8], 'hello', '3', '4', '5')
#
# # числа згенеруються int
# # a += tuple(int(value) for value in input('enter num:').split())
# # # enter num:3 4 5
# # # (1, True, [7, 8], 'hello', 3, 4, 5)
# print(a)
#
# # (int(value) for value in input('enter num:').split())  це генератор списку
# #
# # #!

#-----------------------------------------------

# # користувач вводить назви міст через пробіл, якшо не буде слова Львів, то
# # то місто Львів добавляємо в кінкць кортежу
#
# a = tuple(input('enter city:').split())
# if 'Lviv' not in a:
#     a += ('Lviv', )
# print(a)
# ---------------------------------------------------------

# # якщо Львів є то вирізати
# a = tuple(input('enter city:').split())
# if 'Lviv' in a:
#     i = a.index('Lviv')
#     print(a[:i] + a[i + 1:])
#

t = tuple(name.lower() for name in input('enter text:').split() if 'ро' in name.lower())
print(t)








