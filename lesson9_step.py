# # 1 Сирі стрічки - r -escapeпослідованості не враховуватимуться
# text = r'C:\Users\natal\Desktop\Python\lessons\Nano'
# print(text)
# #----------------------------------------------------------------
#
# # 2 порівняння стрічок
# # ord = покаже код елементу по unicode тфблиці
# print(ord('A'))
# print(ord('a'))
# print('A' > 'a')
# print('Ab' > 'Ac') # порівнюватися буде по b i c
# #------------------------------------------------------------

# # 3
# --- upper -- lower --
# text = 'Hello!'
# print(text.upper())
# print(text.lower())

# user_input= input('enter text: ')
# if user_input.lower() == 'hi':
#     print('work')

# # ---- digit ---
# A
# text = '123'
# if text.isdigit():
#     print('work')

# # B
# x = input('enter number:')
# y = input('enter number:')
# if x.isdigit() and y.isdigit():
#     print(int(x) + int(y))
# else:
#     print('error')

#--------------------------------------------------------

# # 4 -----  JOIN  ----------
# text = 'abc'
# q = '123'
# res= q.join(text)
# print(res)
#-----------------------------------

# # 5
# # ---  REPLACE---
# A
# text = '123-456-789'
# res = text.replace('-', '*') # '-' заміняємо на '*'
# print(res)

# 6 # ----- find ------повертає індекс елемента
# # B
# text = 'dog'
# print(text.find('o'))

#----------------------------------------

# # 7 ------- count шукає кількість співпадінь------
# text = 'ha ha ha hello'
# print(text.count('ha'))
#--------------------------------------------------

# # 8 --- replace ----
# text = input()
# what = input()
# to = input()
# res = text.replace(what, to)
# print(res)
#-------------------------------------------

# # 9 --- remove numbers from sentences
# text = input()
# formatted_txt = ''
# for letter in text:
#     if not letter.isdigit():
#         formatted_txt += letter
# print(formatted_txt)

# # 10 ---- game + random --------
# # randint генерує випадкове число
# # rand choise генерує випадковий текст
#
# import random
# from random import randint, choice
#
# rand_num = random.randint(1, 3)
# rand_text = choice(['Apple', 'Car', 'Keyboard', 'Moon'])
# rand_text_copy = rand_text
# guessed_word = ''
# # print(rand_num, rand_text)
#
# #відобразити слово зірочками
# print(len(rand_text) * '*')
#
# while True:
#     answer = input('answer:')
#     if guessed_word.find(answer) != -1:
#         print('you already try this letter')
#         continue
#     if answer in rand_text:
#         rand_text = rand_text.lower().replace(answer, '*')
#         guessed_word += answer
#         tmp_wod = ''
#     #print(rand_text)
#         for i in range(len(rand_text)):
#             if rand_text[i] == '*':
#                 tmp_wod += rand_text_copy[i]
#             else:
#                 tmp_wod += '*'
#         print(tmp_wod)

# # by using list
# x= list('apple')
# x[1] = '!'
# print(x)
# print(''.join(x))

#------------------------------------------------------------------

# 11 --   L- I  -S - T
# 1 # empty list
# list_value = []
# list_value_2 = list()
#------------------------------------------

# 2 # full list
# list_value = [1, 2, 3, 'hello', True, 4.15]
#
# list_value_2 = list([1, 2, 3])
# print(list_value == list_value_2)
# print(list_value_2)
#
# for val in list_value:
#     print(type(val))
# ------------------------------------

# # 3
# a = [5, 7, 9] * 3
# print(a)

# --------------------------------------

# # 4
# a = [5, 9, 1]
# x, y, z = a
# print(x) # 5
# print(y) # 9
# print(z) # 1
#------------------------------------------------

# # 5
# list_value = [1, 2, 3, 'hello', True, 4.15]
# a = [5, 9, 1]
# #print(a[-1]) # 1
#
# for i in range(len(list_value)):
#     #print(f'index = {i}\tvalue = {list_value[i]}')
#     print(list_value[i])
#
# # i = 0
# # while i < len(list_value):
# #     print(list_value[i])
# #     i += 1

#------------------------------------------------

# # 6 підрахувати суму всіх чисел нашого списку
# мій варіант
# list_value = [10, 2, 3, 4]
# sum = 0
# for i in range(len(list_value)):
#     sum += list_value[i]
# print(sum)

# # другий варіант
# list_value = [10, 2, 3, 4]
# sum = 0
# for i in list_value:
#     sum += i
#     #print(sum)
# print(sum)
# -------------------------------------------

# # 7 згенерувати список з випадкових чисел
# import random
# list_numbers = [random.randint(1, 10) for _ in range(5)]
# print(list_numbers)
#
# #-------------------------------------------

# # # 8 нарізати дані стрічки на список
# text = '12, 14, 17, 33, -2, 6'
# res = text.split(', ')
# #print(res)
# list_n =[int(value) for value in input('enter:').split(' ')]
# # list_n =[int(value) for value in res]
# print(list_n)
# -------------------------------------------
#
# # 9 знайти мін та максим число
# import random
# list_numbers = [random.randint(-100, 100) for _ in range(10)]
# min = list_numbers[0]
# max = list_numbers[0]
# for value in list_numbers:
#     if value > max:
#         max = value
#     elif value < min:
#         min = value
# print(list_numbers)
# print(f'max = {max} min = {min}')

#============================================

# 10
list_users = ['log1', 'password1', 'name1', 'log2', 'pass2', 'name2', 'log3', 'pass3', 'name3']
login = input('enter login:')
password = input('enter password:')
for i in range(0, len(list_users), 3):  # від 0 , звідки, з кроком: 3
    if login == list_users[i]:
        if password == list_users[i + 1]:
            print(f'hello {list_users[i + 2]}')
            break
    #print(list_users[i])

# for v in list_users[::3]:
#     print(v)
# print(list_users[:3])













