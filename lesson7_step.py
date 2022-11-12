# # 1 cancat digit numbers
# repeat = 6
# res = 0
# while repeat > 0:
#     digit = int(input('enter num:'))
#     res = (res * 10) + digit
#     repeat -= 1
# print(res)
#---------------------------------------------------------------------

# # #2 замість прапорців true falseколи перевіряємо чи є шось в циклі
# # # і якщо його нема в циклі то спрацює else
# count = 5
# while count > 0:
#     a = input('enter:')
#     if a == 'stop':
#         break;
#     count -= 1
# else:
#     print('while end')
#---------------------------------------------------------------------

# # #3
# attempts = 3
# rand_num = 3
# is_win = False
# while attempts > 0:
#     input_num = int(input('enter number:'))
#     if input_num == rand_num:
#         print('you win')
#         is_win= True
#         break;
#     attempts -= 1
# if not is_win:
#     print('you loose ')
#---------------------------------------------------------------

# # #4 same like 3 but shorter
# attempts = 3
# rand_num = 3
# while attempts > 0:
#     input_num = int(input('enter number:'))
#     if input_num == rand_num:
#         print('you win')
#         break
#     attempts -= 1
# else:
#     print('you loose ')
#----------------------------------------------------------------

# #5 BANKOMAT
card_1, pin_1, user_name_1, balance_1 = '1111', '1111', 'user1', 1000
card_2, pin_2, user_name_2, balance_2 = '2222', '2222', 'user2', 2000
card_3, pin_3, user_name_3, balance_3 = '3333', '3333', 'user3', 3000

cur_pin, cur_name, cur_balance = '', '', 0
bank_money = 2000
bank_money_bill = 0
withdrawn_count = 0
add_count = 0
balance_count = 0
attempts = 0
while attempts < 3:
    input_card = input('enter card:')
    input_pin = input('enter pin:')
    if input_card == card_1 and input_pin == pin_1:
        cur_pin, cur_name, cur_balance = input_pin, user_name_1, balance_1
        print('user1')
        break
    elif input_card == card_2 and input_pin == pin_2:
        cur_pin, cur_name, cur_balance = input_pin, user_name_2, balance_2
        print('user2')
        break
    elif input_card == card_3 and input_pin == pin_3:
        cur_pin, cur_name, cur_balance = input_pin, user_name_3, balance_3
        print('user3')
        break
    attempts += 1
else:
    print('invalid data')
print(attempts)


while attempts < 3:
    if attempts >= 0:
        print(f'Wellcome {cur_name} ')
        attempts = -1

    choice = int(input('------BANK--------- \n1 - WITHDRAWN\n'
                       '2 - ADD\n'
                       '3 - BALANCE\n'
                       '4 - HISTRY\n'
                       '0 - EXIT\n'
                       '\tEnter your choice:'))

    if choice == 3:
        balance_count += 1
        print(f'\n ---------- BANK--------\n\n\tOn your balance: {cur_balance} usd.\n')
    elif choice == 0:
        print(f'\n ---------- BANK--------\n\n\tGood bye {cur_name} \n')

        break
    elif choice == 2:
        add_count += 1
        money = int(input('enter amount money to add:'))
        if money > 0:
            cur_balance += money
            bank_money += money
            print(f'\n\t successful\nOn your balance: {cur_balance} usd.\n')
        else:
            print('\n\terror \ninvalid value\n')
    elif choice == 1:
        withdrawn_count += 1
        money = int(input('enter amount money to withdraw:'))
        if 0 < money <= cur_balance:
            # pass це заглушка
            if bank_money >= money:
                choice_bill = int(input('\tchoice bill witch u prefer for take a'
                                        ' money:\n\t [500 = 1] or [100 = 2] '
                                        'or [50 = 3] or [20 = 4]'))
                if choice_bill == 1 and money >= 500:
                    cur_balance -= money
                    bank_money -= money
                    bank_money_bill = int(money / 500)

                elif choice_bill == 2 and money >= 100:
                    cur_balance -= money
                    bank_money -= money
                    bank_money_bill = int(money / 100)
                elif choice_bill == 3 and money >= 50:
                    cur_balance -= money
                    bank_money -= money
                    bank_money_bill = int(money / 50)
                elif choice_bill == 4 and money >= 20:
                    cur_balance -= money
                    bank_money -= money
                    bank_money_bill = int(money / 20)

                else:
                    print('error')
                    choice_1 = int(input(' press 1 to return in to menu'))
                    if choice_1 == 1:
                        pass

            else:
                choice = int(input(f'\nnot enough money in bank, we have {bank_money} usd\n'
                                   f'do you want to take it [1 - yes, 2 - no '))
                if choice == 1:
                    cur_balance -= bank_money
                    bank_money -= bank_money

            print(f'\n\t successful\nOn your balance: {cur_balance}  usd\n\t '
                  f'the number of withdrawn bills\n\t in the specified '
                  f'denomination = {bank_money_bill}\n')
        else:
            print('\n\terror \ninvalid value\n')

    elif choice == 4:
        print('history:')
        print(f'balance checked : {balance_count} times\n'
              f'add balance become : {add_count} times\n'
              f'withdraw operations becom :{withdrawn_count} times\n\n\n')


