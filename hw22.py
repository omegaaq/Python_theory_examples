# 1. В текстовому документі зберігається інформація про відвідувачів автомийки.
# Заповніть цей файл інформацією(вручу, не кодом), зчитайте її, та збережіть у колекцію.
# step 0- file info:
# Vlad Vladov
# Oleg Olegovych
# Roman Romanovych
# Olga Olgivna


# step 1
# try:
#     with open('client_info', 'w',encoding='utf-8') as file:
#         file.write('')
# except FileNotFoundError:
#     print('file not founded')

# # step 2
# try:
#     with open('client_info', 'r', encoding='utf-8') as file:
#         res = file.read()
#         print(res)
# except FileNotFoundError:
#     print('file not founded')

# ---------------------------------------------------------
# 2. Зробіть гру на вгадування випадкового числа в діапазоні від 1 до 5. В файлику
# зберігають 3 найкращі результати з ніками користувачів. При запуску гри, показуйте
# найкращі результати. Якщо ви побили якийсь із результатів, Ви вказуєте свій нік. та
# інформація у файлі оновлюється
# # step 1
# try:
#     with open('game_winners_info', 'w', encoding='utf-8') as file:
#         file.write('')
# except FileNotFoundError:
#     print('file not founded')

# step 2
from random import randint

rand_num = randint(1, 5)
print(rand_num)


def write_result_into_file(name):
    try:
        with open('game_winners_info', 'a+', encoding='utf-8') as file:
            file.write('\n' + name)
    except FileNotFoundError:
        print('file not founded')


print('enter num from 1 - 5: you have 5 choices!')
user_name = input('enter your name:')
tryed = 0
while tryed < 5:
    user_choice = int(input('enter num:'))
    tryed += 1
    if user_choice == rand_num:
        tryed_info = str(tryed)
        info_for_file = user_name + ' ' + tryed_info
        print('win')
        if tryed < 3:
            write_result_into_file(info_for_file)
            break
        else:
            print('sorry you lost!')
            break



