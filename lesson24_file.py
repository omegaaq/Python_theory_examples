# # 1 read all text
# file = open('123.txt', 'r', encoding='utf-8')  # r = read
# res = file.read()
# print(res)

# # -----------------------------------
# # 2 readline one line
# file = open('123.txt', 'r', encoding='utf-8')  # r = read
# res = file.readline()
# print(res, end='')

# -----------------------------------
# # 3 readlines повертає список стрічок
# file = open('123.txt', 'r', encoding='utf-8')  # r = read
# res = file.readlines()
# print(res)

# # -----------------------------------
# # 4 tell каже на якій позиції є каретка
# file = open('123.txt', 'r', encoding='utf-8')
# print(file.tell())
# file.readline()
# print(file.tell())
# file.readline()
# print(file.tell())

# # -----------------------------------
# # 4 seek поставити каретку в певну позицію і зчитувати текст з звданого байту
# file = open('123.txt', 'r', encoding='utf-8')
# file.seek(1)
# r = file.readline()
# print(r)

# # -----------------------------------
# # 5 close
# file = open('123.txt', 'r', encoding='utf-8')
# file.seek(1)
# r = file.readline()
# print(r)
# file.close()

# -----------------------------------
# # 6 try catch for file
# try:
#     file = open('123.txt', 'r', encoding='utf-8')
#     try:
#         res = file.read()
#         print(int(res))
#     except ValueError:
#         print('text is not a numeric')
#     finally:
#         file.close()
# except FileNotFoundError:
#     print('file not founded')

# ----------------------
# # 7 try catch for file + with
# # with це менеджер контексту він сам закриває файл
# try:
#     with open('123.txt', 'r', encoding='utf-8') as file:
#          res = file.read()
#          print(int(res))
# except FileNotFoundError:
#     print('file not founded')

# ----------------------------------------------------------
# # 8
# try:
#     with open('123.txt', 'r', encoding='utf-8') as file:
#         #res = file.read().split('\n')
#         res = file.readlines()
#         print(*res)
# except FileNotFoundError:
#     print('file not founded')

# ----------------------------------------------------------
# # 9
# try:
#     with open('123.txt', encoding='utf-8') as file:
#         data = tuple()
#         for value in file.read().split('\n\n'):
#             res = value.split('\n')
#             data += ({
#                 'country': res[0],
#                 'capital': res[1],
#                 'population': float(res[2]),
#                 'neighbors': res[3].split()
#
#             }, )
#
# except FileNotFoundError:
#     print('file not founded')
# print(data[0]['neighbors'])
# -----------------------------------------------

# #   ---------     Режими длступу до файла w,a,r, a+  -----------------------

# # 10 'w' ===  записуємо у файл, попередню інфу стирає
#  в цьому режимі зчитувати інфо з файла не можна
# try:
#     with open('123.txt', 'w', encoding='utf-8') as file:
#         file.write('123')
# except FileNotFoundError:
#     print('file not found')

# ---------------------------------------

# # 11 'a' ===   записуємо у файл, попередню інфу стирає, алe
#  в цьому режимі зчитувати інфо з файла не можна
# try:
#     with open('123.txt', 'a', encoding='utf-8') as file:
#         file.write('123')
# except FileNotFoundError:
#     print('file not found')

# -----------------------------------------

# # 12
# try:
#     with open('123.txt', 'a', encoding='utf-8') as file:
#         file.write(input() + '\n')
# except FileNotFoundError:
#     print('file not found')
#
# # -----------------------------------------------

# # 13
# try:
#     with open('123.txt', 'a', encoding='utf-8') as file:
#         file.write(input() + '\n')
#         file.read()
# except FileNotFoundError:
#     print('file not found')
#
# # -----------------------------------------------

# # # 14 'a+' === можна і записівати і считувати дані,
# # але має бути seek(0)
# try:
#     with open('123.txt', 'a+', encoding='utf-8') as file:
#         file.write(input() + '\n')
#         file.seek(0)
#         res = file.read()
#         print(res)
# except FileNotFoundError:
#     print('file not found')
#
# # # -----------------------------------------------

# # 15
# try:
#     with open('123.txt', 'a', encoding='utf-8') as file:
#         file.write(input() + '\n')
#         file.read()
# except FileNotFoundError:
#     print('file not found')
#
# # -----------------------------------------------

# # cafe booking place
# step 1 create files
# try:
#     with open('place_specification.txt', 'w', encoding='utf-8') as file:
#         file.write('')
# except FileNotFoundError:
#     print('file not found')

# step 2 create files
# try:
#     with open('event_info.txt', 'w', encoding='utf-8') as file:
#         file.write('')
# except FileNotFoundError:
#     print('file not found')

# step 3

def read_file(file_name):
    pass


def write_file(file_name, *args, **kwargs):
    pass


def menu_validation(number):
    if 0 <= number <= 5:
        return True
    return False

def free_tables():
    pass

def book_table(file_name, *args, **kwargs):
    pass


place_cpecification = read_file('place_specification.txt')

while True:
    try:
        menu_choice = int(input('\t*** rezerv ***\n1 -book\n2 - update\n3 - canceled\n\n'
                                '\t*** info ***\n4 - available\n5 - full\n0 - Exit\n'
                                'Enter your choice:'))
    except ValueError:
        print('enter a number!')
        continue
    if menu_validation(menu_choice):
        if menu_choice == 4:
            free_tables()
        elif menu_choice == 1:
            pass




# Реалізуйте в завданні з уроку 1, 3, 5 пункт з меню.
# Детальне уточнення є на завершенні уроку у повторі в тімсі)


