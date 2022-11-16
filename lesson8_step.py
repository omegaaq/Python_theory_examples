#  ----------- cycle FOR -------
# # 1 просто пройтися по числам циклу
# for x in 3, 7, 13, 22, 56, -2, -9, 5:
#     print(x)
#----------------------------------------------------------
# # 2 пройтися по слову
# text = input('enter text:')
# i = 0
# for letter in text:
#     print(f'{i= }\t{letter= }')
#     i +=1
#-------------------------------------------------------

# # ------- range -------
# # 3 показати задані числа в діапазоні (from 0 to 4)
# for i in range(5):
#     print(i)
#-----------------------------------------------------------

# 4  таке ж як і 3 завдання просто неформальна форма запису
# for _ in range(5):
#     print('hello')
#---------------------------------------------------

# 5 покаже від 3 до 6
# for i in range(3,7):
#     print(i)
#---------------------------------------------------

# # 6 покаже від 5 , 10, 15 (тобто числа від 5 до 20 але з кроком збільшення на 5)
# for i in range(5, 20, 5):
#     print(i)
#----------------------------------------------------------------------

# # 7
# text = 'hello'
# print(text[0]) #// h
# print(text[4]) #// 0
# #print(text[5]) #// mistake index ou of range
# print(text[-1]) #// o з кінці передаватиметься
# print(text[-5]) #// h
#---------------------------------------------

# # 8 вивести циклом слово по літерам
# text = 'hello'
# i = 0
# while i < 5:
#     print(text[i])
#     i += 1

#--------------------------------------------------------------

# # 9 вивести циклом слово по літерам
# text = 'hello'
# for letter in text:
#     print(letter)
#--------------------------------------------------

# # 10 підрахувати кількість літер у стрічці
# text = input('enter text:')
# symb = input('enter symb to count')
# count = 0
# for value in text:
#     if value == symb:
#         count += 1
# print(f'{count=}')
#---------------------------------------------------

# # 11
# text = input('enter text:')
# symb = input('enter symb to count')
# count = 0
# #print(symb in text)
# if symb in text:
#     for value in text:
#         if value == symb:
#             count += 1
# print(f'{count=}')

#------------------------------------------------

# # 12
# text = 'abracadabra'
# #text[2] = 'c' # !стрічка це константна змінна і отак змінити її не можна!
# print(text)
# print(text[3:5]) #показати з 3 по 5 індекс -- ас
# print(text[:5]) #показати від початку до 5 індексу
# print(text[5:]) #показати від 5 індексу до кінця

#--------------------------------------------

# # 13 find letter
# text = 'abracadabra'
# index_1 = 0
# first = input('Enter:')
# second = input('Enter:')
#
# if first in text and second in text:
#     for i in range(len(text)):
#         print(f'{first} == {text[i]}')
#         if first == text[i]:
#             index_1 = i
#             break
# --------------------------------------------

# # 14 find word start from 1 letter and end with another letter and show that
# # text = 'abracadabra'
# text = input('enter text: ')
# first = input('Enter:')
# second = input('Enter:')
#
# if first in text and second in text:
#     for i in range(len(text)):
#
#         if first == text[i]:
#
#             for j in range(i+1, len(text)):
#                 if second == text[j]:
#                     print(text[i:j+1])
#                     break
#             break
#----------------------------------------------------

# # 15 multiplication table from 1 to 10:
# size = int(input('enter size:'))
# for i in range(1, size+1):
#     for j in range(1, size+1):
#         print(i * j, end='\t')
#     print()

# ------------------------------------------------

# # 16
# #       012345678910
# text = 'abracadabra'
# print(text[2:7:2]) # від якого числа : по яке число : і з яким кроком = rcd

#--------------------------------------------------------

# # 17
# A
# msg_text = input('enter text:')
# price = 2
# count = 0
# for _ in msg_text:
#     count += 1
# print(count * price)

# # B
# msg_text = input('enter text:')
# price = 2
# print(len(msg_text) * price)

#---------------------------------

# 18 change letters on some another letter
new_text = ''
text = 'abracadabra'
for letter in text:
    if letter == 'a':
        new_text += '!'
        continue
    new_text += letter
print(new_text)










