# СЛОВНИКИ
# дані зберігаються не по індексу а по ключу
# змінні значення не можуть використовуватися як ключі
import copy

# #  Поміняти літеру і стрічці
# a = 'asd'
# b = ''
# for i in a:
#     if i == 'a':
#         b += 'b'
#         continue
#     b += i
#
# print(b)  # bsd
# print(a)  # asd
#-----------------------------------------------------------------

# ----DICTIONARY

# # 1
# a = dict()
# print(a)
#-------------------------------------------

# 2 наповнюємо словник
# # a:
# a = dict(one='hello')  # one -> this is key
# print(a)

# # b:
# a = {
#     'one': 'hello',
#     2: 'bye',
#
# }
#----------------------------------------------

# 3 Досткпаємося до значення словника
# a = {
#     'one': 'hello',
#     2: 'bye'
# }
# print(a['one'])
# print(a[2])

# user = {
#     'name': 'Vlad',
#     'age': 18,
#     'isMarried': False,
#     'languages': ['ukr', 'eng', 'spanish']
# }
# print(user['name'])
# print(user['languages'])
# if 'city' in user:
#     print(user['city'])
# else:
#     print('city is not found')

#-------------------------------------------------

# # SETDEFAULT
# створює ключ якшо він не існує і можна його одразу наповнити
#  можна отримати дані які знаходяться за вказаним ключем
# повторне значення по ключу ы даних  !НЕ ПРИСВОЮЄ
# user = {
#     'name': 'Vlad',
#     'age': 18,
#     'isMarried': False,
#     'languages': ['ukr', 'eng', 'spanish']
# }
#
# print(user.setdefault('languages'))
# print(user.setdefault('city'))   # NONE
# print(user.setdefault('city', 'Lviv'))
# print(user)
# # {'name': 'Vlad', 'age': 18,
# # 'isMarried': False,
# # 'languages': ['ukr', 'eng', 'spanish'],
# # 'city': 'Lviv'}

#---------------------------------------------------------------

# # добавляємо дані в ключ
# user = {
#     'name': 'Vlad',
#     'age': 18,
#     'isMarried': False,
#     'languages': ['ukr', 'eng', 'spanish']
# }
# print(user.setdefault('city', 'Lviv'))
# user['test'] = 'text'
# print(user)

#------------------------------------------------

#
# # міняємо дані в ключі
# print(user['age'])  # 18
# user['age'] = 90
# print(user['age'])  # 90

# # GET доступитися до ключа і помилки не провокуватиме якшо ключа немає
# user = {
#     'name': 'Vlad',
#     'age': 18,
#     'isMarried': False,
#     'languages': ['ukr', 'eng', 'spanish']
# }
# print(user.get('age'))
# print(user.get('ttt'))
# print(user)

#---------------------------------------------------

# # POP , POPITEM видаляється останній елемент із словника і повертає кортеж
# user = {
#     'name': 'Vlad',
#     'age': 18,
#     'isMarried': False,
#     'languages': ['ukr', 'eng', 'spanish']
# }
#
# x = user.popitem()
# print(x[0])
# print(x[1])
# print(user)

# --------------------------------------------------------

# # POP - якшо шось передаєм то нам видаляється за цим значенням,
# # а якшо нічого не передаєм тут  то буде помилка
# user = {
#     'name': 'Vlad',
#     'age': 18,
#     'isMarried': False,
#     'languages': ['ukr', 'eng', 'spanish']
# }
# x = user.pop('age')
# print(x)  # 18
# print(user)

#---------------------------------------------------------------

# # KEYS
# user = {
#     'name': 'Vlad',
#     'age': 18,
#     'isMarried': False,
#     'languages': ['ukr', 'eng', 'spanish']
# }
# x = user.keys()
# print(x)
#
# for key in user.keys():
#     print(key)

#------------------------------------------------

# VALUES
# user = {
#     'name': 'Vlad',
#     'age': 18,
#     'isMarried': False,
#     'languages': ['ukr', 'eng', 'spanish']
# }
# for v in user.values():
#     print(v)

#-------------------------------

# # ITEMS\
# # 1
# user = {
#     'name': 'Vlad',
#     'age': 18,
#     'isMarried': False,
#     'languages': ['ukr', 'eng', 'spanish']
# }
# for key, v in user.items():
#     print(f'key = {key}\tvalue = {v}')


# # # 2
# print({'1': 'abc', '2': 'qwerty' }.items())  # dict_items([('1', 'abc'),
#                                             # ('2', 'qwerty')])


# ----------------------------------------------

# # CLEAR
# user = {
#     'name': 'Vlad',
#     'age': 18,
#     'isMarried': False,
#     'languages': ['ukr', 'eng', 'spanish']
# }
# user.clear()
# print(user)

#-------------------------------------
# # COPY
# user = {
#     'name': 'Vlad',
#     'age': 18,
#     'isMarried': False,
#     'languages': ['ukr', 'eng', 'spanish']
# }
# # # variant 1
# # x = dict(user)
# # print(x)
# # print(id(x))
# # print(id(user))
#
# # variant 2
# x = user.copy
# print(x)
# print(id(x))
# print(id(user))
#
# #---------------------------------------------

# # COPY ссилку/ посилання
# user = {
#     'name': 'Vlad',
#     'age': 18,
#     'isMarried': False,
#     'languages': ['ukr', 'eng', 'spanish']
# }
#
# x = user
# print(x)
# print(id(x))
# print(id(user))
#
# #---------------------------------------------

# # COPY ссилку
# user = {
#     'name': 'Vlad',
#     'age': 18,
#     'isMarried': False,
#     'languages': ['ukr', 'eng', 'spanish']
# }
#
# x = user
# print(x)
# print(id(x))
# print(id(user))
#
# #---------------------------------------------

# x = 13
# y = 17
# temp = x #13
# x = y #17
# y = temp #13
# print(id(x))
# print(id(y))
#------------------------------------------

# # Обєднуємо словники
# a = {
#     1: 'a',
#     'hi': 'hello'
# }
#
# b = {
#     2: 'b',
#     'hi': 'bye'
# }
#
# c = a | b
# print(c)  # {1: 'a', 'hi': 'bye', 2: 'b'}

#----------------------------------------------

# # SETDEFAULT APPEND
# user = {
#     'name': 'Vlad',
#     'age': 18,
#     'isMarried': False,
#     'languages': ['ukr', 'eng', 'spanish']
# }
# a = user.setdefault('lang', ['ukr', 'eng', 'spanish']).append('he')
# print(a)
# print(user)

#------------------------------------------------
# #JOIN
# user = {
#     'name': 'Vlad',
#     'age': 18,
#     'isMarried': False,
#     'languages': ['ukr', 'eng', 'spanish']
# }
# a = user.setdefault('lang', ['ukr', 'eng', 'spanish']).append('1233456')
# #
# # for value in user.values():
# #     print(value)
#
# res = ' -*- '.join(user['lang'])
# print(res)

#-------------------------------------------

# словник конверткє з якогось числа в число азбуки морзе
# shift + alt
# morse = {
#     1: '.____',
#     2: '..___ ',
#     3: '...__',
#     4: '...._',
#     5: '.....',
#     6: '_....',
#     7: '__...',
#     8: '___..',
#     9: '____.',
#     0: '_____'
# }
# num = input('enter num:')
# # variant 1
# # for x in num:
# #     print(morse[int(x)], end=', ')

# # variant 2
# lst = list(morse[int(x)] for x in num)
# # print(lst)
# # print(*lst)
# print(', '.join(lst))

#--------------------------------------------

# # A
# a = dict()
# print(a.setdefault('1', []))  # []
# a['1'] = 'hello'
# print(a.setdefault('2', ['one', 'two']))  #['one', 'two']
# b = a.setdefault('2', ['one', 'two']).append('he')
# print(a)  # {'1': 'hello', '2': ['one', 'two', 'he']}

# # B
# a = {
#     ('12', '21'): 'hello'
# }
# print(a[('12', '21')])  # hello


#===================================================
# # user вводить день народженні імя, якшо дні народження співпадають
# # то ми формуємо список цих користувачів з повтореним днем народження
# a = dict()
# for _ in range(3):
#     text = input('enter day and name:').split()
#     #в словник а присвоюю(setdefault) під індексом text[0]
#     # + [] пустий список i (append) добавляєм text[1] це ымя юзера
#     a.setdefault(text[0], []).append(text[1])
# #   print(a)
# # # print(a)
# for key, value in a.items():
#     print(f'{key}: {", ".join(value)}')













