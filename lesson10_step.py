# 1
# lst = [False, 'hello', 13]

# # append ----------add in the end of list
# lst.append(3.14)
# print(lst)
# print(*lst)

# #insert ------- add smthng in some position
# lst = [False, 'hello', 13]
# lst.insert(0, 'text') # 0 this is position
# print(lst)

# # 2 two list togather
# lst = [False, 'hello', 13]
# lst_2 = [13, 'hi']
# lst += lst_2
# print(*lst)

# # extend ----------add in the end
# lst = [False, 'hello', 13]
# lst_2 = [13, 'hi']
# lst.extend(lst_2)
# print(lst)

# # 3 remove ------------ delete only 1 first element
# lst = [False, 'hello', 13, '13', 13]
# value = '13'
# if value in lst:
#     lst.remove('13')
# else:
#     print('not found')
# print(lst)
# -----------------------------------

# # 4 index ------------
# lst = [False, 'abc', 'hello', 13, '13', 13]
# value = 'abc'
# if value in lst:
#     print(lst.index(value))
# else:
#     print('not found')
# ---------------------------------

# # 5 pop ------------ deleted last element or element by index
# lst = [False, 'abc', 'hello', 13, '13', 13, 'hi']
# deleted_value = lst.pop()
# deleted_value = lst.pop(1)
# print(deleted_value)
# print(lst)
# ---------------------------------------------

# # 6 count підраховує кть (знаходжень)входження чогсь у нашому списку
# lst = [False, 'abc', 'hello', 13, '13', 13, 'hi']
# value = lst.count(13)
# print(value)
# ------------------------------------

# # 7 ---- len, -------- min, --------- max ---------clear
# lst = [False, 'abc', 'hello', 13, '13', 13, 'hi']
# lst.clear()
# lst1 = [23, 12, -2, 0]
# # print(len(lst))
# print(min(lst1))
# print(max(lst1))
# -----------------------------------------

# # 8 ------------sort сортує по зростанню
# lst1 = [23, 12, -2, 0]
# lst1.sort()
# print(*lst1)
# #--------------------------------------

# # 9 -------- sorted ---повертаж новий відсортований список
# lst1 = [23, 12, -2, 0]
# x = sorted(lst1)
# print(*x)
# print(*lst1)
#---------------------------------

# # 10 ------------ reverse
# lst1 = [23, 12, -2, 0]
# lst1.sort(reverse=True)
# print(*lst1)
# # ------------------------------------
#
# # 11 в змінній x збеігається ссилка на область памяті lst1
# lst1 = [23, 12, -2, 0]
# x = lst1
# lst1[0] = 'hello'
# print(lst1)
# print(x)
# #--------------------------

# # 12 щоб зробити повноцінну копію списку:
# lst1 = [23, 12, -2, 0]
# # # v1
# # x = list(lst1)
#
# # v2
# x = lst1.copy()
#
# lst1[0] = 'hello'
# print(lst1)
# print(x)

# ----------------------------------

# # 13 одною стрічкою через пробіл ввести числа
# # і відсортувати їх ц порядку спадання
# list_n =[int(value) for value in input('enter:').split('')]
# list_n.sort(reverse=True)
# print(list_n)
# ---------------------------------

# # 14 в нас є існуючий список , користувач вводить перелік продуктів в новий список
# #цей новий список треба добавити до існуючого в кінець
# lst = ['apple', 'plump', 'bananas', 'watermelon']
# user_input_lst = [str(value) for value in input('enter products ').split()]
# lst += user_input_lst
# print(*lst)
# #------------------------

# # 15 змінити в стрічці букви
# txt = 'abracadabra'
# lst = list(txt)
# lst[0] = '!'
# lst[6] = '*'
# txt = ''.join(lst)
# print(txt)
# #-----------------------------

# # 16 split шоб кожен елемент який введеться розділити по пробілу
# print(input().split())
#------------------------------------------

# # 17 підрахувати середню арифm суму чисел
# lst = [int(value) for value in input('enter: ').split()]
# res = sum(lst) / len(lst)
# print(round(res, 1))
# #--------------------------------------------

# # # 18 гра хрестики нолики
# # #lst_field = [0, -1, 1, 0, 0, -1, 1, 0, -1]
# # while True:
# #     print(lst_field)
# #     for i in range(len(lst_field)):
# #         if lst_field[i] == -1:
# #             print('*', end='  ')
# #         elif lst_field[i] == 0:
# #             print('o', end='  ')
# #         else:
# #             print('x', end='  ')
# #         if i == 2 or i == 5:
# #             print()
# #     input('\n\n1  2  3\n4  5  6\n7  8  9\nEnter ur choice:')

# # # #  working variant
# lst_field=[]
# for _ in range(3):
#     lst_field.append([-1, -1, -1])
# print(lst_field)
#
# while True:
#     for i in range(3):
#         for j in range(3):
#             if lst_field[i][j] == -1:
#                 print('*', end='  ')
#             elif lst_field[i][j] == 0:
#                 print('o', end='  ')
#             else:
#                 print('x', end='  ')
#         print()
#     choice = [int(value) for value in input('enter row and col: ').split()]
#
#     if choice.isdigit() and int(choice) in range(1, 10):
#         pass
#     else:
#         print('\n\tenter a number:\n')

# # 19 --як отримати елементи зі списку листа
# l = list[['a', 'b', 'c'], [1, 2, 3]]
# print(l[1][0])  # => 1
# print(l[0][0])  # => 'a'









