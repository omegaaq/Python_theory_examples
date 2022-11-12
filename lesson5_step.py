# #1
# x = 5
# if x>10:
#     x=15
# else:x=0
#
# # тернарний оператор
# # результат повертається в якусь змінну
# x = 15 if x > 10 else x = 0
# # x = 15 if x > 10 else print(x)

# # 2
# num = input('enter number:')
# text = 'even' if num % 2 == 0 else print('not even')
# print(text)
#
# print(input('enter num:'))

# # 3
# num1 = int(input('enter num1:'))
# operation = input('enter operator:')
# num2 = int(input('enter num1:'))
# # res = num1 + num2 if operation == '+' else num1 - num2
# # print(res)
# if operation == '+':
#     res = num1 + num2
# else:
#     if operation == '-':
#         res = num1 - num2
#     else:
#         if operation == '*':
#             res = num1 * num2
#         else:
#             print('incorrect')
# print(res)

# # 4
# login = '12'
# correct_info = True if login == '12' else False
# print(correct_info)

# # 5
# a = True
# if not a:
#     print(a)

# 6
# --------- CYCLE ------
# # 1
# while True:
#      print('a')

# # 2
# i = 0
# while i < 5:
#     print(i)
#     i += 1

# # 3
# i = 0
# while i < 5:
#     print(i)
#     if i == 3:
#         i = 7
#     i += 1
# print(i)

# # 4
# start = int(input('enter start:'))
# end = int(input('enter end:'))
# while start <= end:
#     start +=1

# # 5
# count = int(input('enter num: '))
# # i = 0
# # while i < count:
# #     print('work')
# #     i += 1
# while count > 0:
#     print('work')
#     count -= 1

# # 6 ----- переприсвоення --------
# #  -- A
# x, y = 13, 17
# print(x, y)
# x, y = y, x
# print(x, y)
#
# # -- B  bad example
# x, y = 13, 17
# x = y #17
# y = x #17
# print(x, y)

# #--- c good example
# x, y = 13, 17
# temp = x #13
# x = y #17
# y = temp #13
# print(x, y)

# # 7 сумма чисел в діапазоні заданому
# start = int(input('enter start:'))
# end = int(input('enter end:'))
# sum = 0
# #while start < end + 1:
# while start != end + 1:
#     print(f'sum = {start}')
#     sum += start
#     start += 1
# print(f' sum = {sum}')

# # 8
# num = int(input('enter number:'))
# count = 0
# while num:
#     num //= 10
#     # count підраховує скільки раз операція ділення по модулюю тривала
#     count += 1
# print(f'count = {count}')

# 9
i = 0
max_num = 0
while i < 3:
   num = int(input('enter num:'))
    #max_num = num if i == 0 else num
   if i  == 0:
       max_num = num
   elif num > max_num:
       max_num = num
   i += 1
print(max_num)


