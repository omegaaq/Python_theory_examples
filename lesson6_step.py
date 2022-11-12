# # 1 сумма чисел в діапазоні заданому
# start = int(input('enter start:'))
# end = int(input('enter end:'))
# sum = 0
# #while start < end + 1:
# while start != end + 1:
#     print(f'sum = {start}')
#     sum += start
#     start += 1
# print(f' sum = {sum}')
#----------------------------------------
# # 2
# x = 10
# while x != 0:
# #while x >= 0:
#     print(x)
#     x -= 1
# -------------------------------------
# print('*' + ' ' + '*')
# print('* ' * 3)
# --------------------------------------
# # 3
# # reverce triangle
# num = int(input('enter number:'))
# while num > 0:
#     print('* ' * num)
#     num -= 1
# ---------------------------------------
# # 4
# # normal triangle
# i = 1
# num = int(input('enter number:'))
# while i <= num:
#     print('* ' * i)
#     i += 1
# --------------------------------------------
# # 5
# # normal triangle
# num = int(input('enter number:'))
# text = ''
# while num > 0:
#     text += '* '
#     print(text)
#     num -= 1
# --------------------------------
# # # 6
# # rectangle, kub
# num = int(input('enter number:'))
# # tmp_num = num
# # num = tmp_num
# i = num
# while num > 0:
#     print('* ' * i)
#     num -= 1
# -------------------------
# # #  6
# # # rectangle, kub inside free
# num = int(input('enter number:'))
# tmp_num = num
# num = tmp_num
# i = num
# while i > 0:
#     if i == num or i == 1:
#         print('*  ' * num)
#     else:
#         print('*  ' + '   ' * (num - 2) + '*')
#     i -= 1
# ----------------------------------------------------------------------------

# ----- operators BREAK and CONTINUE
# ------ use only in cycles
# # 1  stop the cckle
# count = 0
# text = ''
# while True:
#     word = input('enter word:')
#     text += word + ', '
#     count += 1
#     if word == 'stop':
#         print('while end')
#         print(count)
#         break
#     #break cycle will not work
# ---------------------

# # 2
# repeat = 0
# count = 0
# text = ''
# while True:
#     repeat += 1
#     word = input('enter word:')
#     if word == 'stop':
#         print('while end')
#         # не дійде до однієї ітерації
#         print(f'count ={count}')
#         break
#     text += word + ', '
#     count += 1
# print(f'repeat = {repeat}')

# ---------------------

# # 3
# repeat = 0
# count = 0
# text = ''
# word = ''
# while word != 'stop':
#     repeat += 1
#     word = input('enter word:')
#     if word == 'stop':
#         print('while end')
#         print(f'count ={count}')
#     text += word + ', '
#     count += 1
# print(f'repeat = {repeat}')

#----------------------------------
#
# # 4
# count = 0
# sum = 0
# while True:
#     num = int(input('enter number:'))
#     count +=1
#     sum += num
#     if sum > 50:
#         print(f'count = {count} \n sum = {sum}')
#         break
#
# # #----------------------------------
#
# # 5 same like 4 but without break буде вічний цикл
# count = 0
# sum = 0
# while True:
#     num = int(input('enter number:'))
#     count +=1
#     sum += num
#     if sum > 50:
#      print(f'count = {count} \n sum = {sum}')

# # #----------------------------------
#
# # 6 same like 4 but without break
# count = 0
# sum = 0
# while sum <= 50:
#     num = int(input('enter number:'))
#     count +=1
#     sum += num
# print(f'count = {count} \n sum = {sum}')

# #----------------------------------

# # 7 same like 4 but without break
# x = 10
# while x > 0:
#     x -= 1
#     if x % 2 == 0:
#         print(f'{x}\n')
#         continue
#     print(f'{x}\n')
#     # print(x)

#--------------------------------

# # 8
# while True:
#     num = int(input('enter num:'))
#     if num == 0:
#         break
#     elif num % 2 == 0:
#         continue
#     print(num)
#
# 9
#reverse number
# i = 0
# str_sum = ''
# while i < 3:
#     i += 1
#     num = int(input('enter num'))
#     str_num = str(num)
#     str_sum += str_num
#     int_sum=int(str_sum)
# print(str_sum)












