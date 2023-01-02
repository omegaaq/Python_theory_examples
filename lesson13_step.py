# #1
# lst_users = [
#     {
#         'login': 'test@ua',
#         'password': '123',
#         'name': 'Testio'
#
#     },
# {
#         'login': 'test1@ua',
#         'password': '123',
#         'name': 'Test_name'
#
#     }
#
# ]
# # print(lst_users[0].__getitem__('login'))  # # test@ua
# print(lst_users[0]['login'])  # test@ua
#
#
# while True:
#     choice = input('enter 1 =  Login 2 = Registration \n Enter your choice: ')
#     login = input('enter login:')
#     password = input('enter password:')
#
#     if choice == '1':
#         for user in lst_users:
#             if user['login'] == login and user['password'] == password:
#                 print(f'hello {user["name"]}')
#                 break
#         # else пишемо тут тому шо якшо не виконається if і не спраціює break
#         # то цей elseспрацює тоді коли не спрацює break
#         else:
#             print('user not found')
#     elif choice == '2':
#         name = input('enter name: ')
#         for user in lst_users:
#             if user['login'] == login:
#                 print('this login is already used')
#                 break
#         else:
#             lst_users.append(
#                 {
#                     'login': login,
#                     'password': password,
#                     'name': name
#                 }
#             )
#             # print('success')
#             print(lst_users)
#-------------------------------------------------------------------------

# # 2
# # створити пустий словник
# a = {}
#
# #--------------------------------------------------------------------------

# # # -----------МНОЖИНИ-----
# не впорядкована колекція не повторюваних даних
#  по index-у не пройдемося
# можна змінювати, алe не можна зберігати в них змінні типи даних( list, dicionary)
# в множинах зберігаємо : str , int, bool, kortej

# 1 # створити пусту множину
# a = set()
# print(type(a))

# ------------------------------------------

# # 2 наповнити множину
# b = {'Oleg', 1, 'Vlad', 1}
# print(b)  # {1, 'Oleg', 'Vlad'}
#
# for value in b:
#     print(value)

# ----------------------------------------------

# # === ADD добавляє шось одне====
# a = set()
# a.add(input('enter info :'))
# print(a)
# # ---------------------------------

# # === REMOVE====видаляє і  помилку викидає
# a = {1, 2, 3}
# a.add('abc')
# print(a)
# a.remove(7)
# print(a)
# # ---------------------------------

# # === DISCARD==== видаляє і  помилку !  НЕ ! викидає
# a = {1, 2, 3}
# a.discard(7)
# print(a)
# # ---------------------------------

# # === POP==== видаляє  хаотично останній елемент
# a = {1, 2, 3, 'abc'}
# x = a.pop()
# print(x)
# print(a)
# # ---------------------------------

# # === CLEAR====
# a = {1, 2, 3}
# a.clear()
# print(a)
# # ---------------------------------

# # ---- UPDATE -----добавляє декілька елементів
#
# a = {1, 2, 3}
# a.update([5, 8, 10,('hello', 'bye')])
# print(a)
#
# #--------------------------------------------

# #-----DIFERENCE ------порівняє і покаже шо у нас немає в множині b
# a = {1, 2, 3}
# b = {3, 4, 5}
# c = a.difference(b)  # {1, 2}
# print(c)
#
# #-----------------------------------------

# #-----INTERSECTION ------порівняє і покаже шо у нас є спільне в множині b
# a = {1, 2, 3}
# b = {3, 4, 5}
# c = a.intersection(b)  # {1, 2}
# print(c)  # 3
#
# #-----------------------------------------

# # користувач вводить стрічку, з неї треба дістати числа,
# # посортувати їх і вивести через пробіл
#
a = {value for value in input('enter text: ') if value.isdigit()}
print(*a if a else ['missing'])

# #-------------------------------------------------


# # У пості, один користувач може залишати декілька коментарів,
# # підрахуйте к-сть унікальних користувачів у коментарях,
# # коли дані чату зберігаються у наступному форматі списку.
#
# lst = ['Vlad: hello all',
#        'Max: qq', 'Vlad: how are u?',
#        'Mia: cool weather!',
#        'Max: approve']
# # генеруєм множину
# # split(':') розділяємо 'Max: qq',
# a = {value.split(':')[0] for value in lst}
# print(a)
#
# # a1 = 'vlad:123'.split(':')
# # print(a1[0])

#-----------------------------------------------------


