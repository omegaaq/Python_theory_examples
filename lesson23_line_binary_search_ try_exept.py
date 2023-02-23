# SEARCH

from random import randint

# def generate_lst():
#     l = []
#     for _ in range(21):
#         #count = 0
#         while True:
#             rand_num = randint(-10, 10)
#             #count += 1
#             if rand_num not in l:
#                 l.append(rand_num)
#                 break
#         #print(count)
#     return l


# lst = generate_lst()
# print(lst)

# # # 1 лінійчний пошук
# num = int(input('enter num:'))
# for x in lst:
#     if x == num:
#         print('found')
#         break
# ----------------------------------------------------------------

# # # 2 binary search
# def binary_search(list_n, ele):
#     begin_index = 0
#     last_index = len(list_n) - 1
#     while begin_index <= last_index:
#         mid = (begin_index + last_index) // 2
#         if list_n[mid] == ele:
#             return mid
#         elif ele > list_n[mid]:
#             begin_index = mid + 1
#
#         else:
#             last_index = mid - 1
#     return None
#
#
# rand_data = [randint(-20, 20) for _ in range(randint(10, 20))]
# print(rand_data)
# rand_data = sorted(rand_data)
# print(rand_data)
# print(binary_search(rand_data, int(input())))

# 3 ---- try ---- exept
# print('a')
# try:
#     5/0
#     print('hello'[10])
# except IndexError:
#     print('incorrect index')
# except ZeroDivisionError:
#     print('stop do it')
# print('b')

# -----------------------------------------------

# # 4
# print('a')
# try:
#     5/0
#     print('hello'[10])
# except (IndexError, ZeroDivisionError):
#     print('incorrect value')
#
#
# print('b')

# -----------------------------------------------------

# # 5
# try:
#     num = int(input('num:'))
#     print(f'num = {num}')
# except ValueError:
#     print('enter number!')

# -------------------------------------------------------

# # 6
# while True:
#     try:
#         num = int(input('num:'))
#     except ValueError:
#         print('its not a number')
#     else:
#         print(num)
#         break

# -----------------------------------

# # 7 var 1
# lst = ['Stepan', 13, False, 28, 89, 'Hi']
# while True:
#     try:
#         num = int(input('num:'))
#         try:
#             print(lst[num])
#         except IndexError:
#             print('incorrect index')
#     except ValueError:
#         print('not a number')
#
#     else:
#         break

# ------------------------------------------------------
# # 7 var 2
# lst = ['Stepan', 13, False, 28, 89, 'Hi']
# while True:
#     try:
#         try:
#             num = int(input('num:'))
#             print(lst[num])
#             break
#         except IndexError:
#             print('incorrect index')
#     except ValueError:
#         print('not a number')
#
#
# # ----------------------------------------

# 8 --------  FILE -----------
file = open('123.txt', encoding='utf-8')
res = file.read()
res2 = file.readline()
res3 = file.readlines()
print(res)
