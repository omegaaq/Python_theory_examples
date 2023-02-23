# # cafe booking place
# ------  step 1 create files -----------
# try:
#     with open('place_specification.txt', 'w', encoding='utf-8') as file:
#         file.write('')
# except FileNotFoundError:
#     print('file not found')

# --------------  step 2 create files  -----------------------
# try:
#     with open('event_info.txt', 'w', encoding='utf-8') as file:
#         file.write('')
# except FileNotFoundError:
#     print('file not found')

# ------------   step 3 ----------
# book - 1
def book_tables(specification, event_data):
    result = True
    free_tables(specification,event_data)

    table = input('enter table:')
    for key, value in specification.items():
            if table in value:
                print(f' you reserved table number {table}')
                value.remove(table)
                print('new information about free tables')
                free_tables(specification, event_data)
            else:
                print(f'table number {table} is rezerved already')
# -------------------------------------------------------------------------


# 5 full
def full_tables(specification, event_data):
    for key_event, value_event in event_data.items():
        print(f'reserved tables: {key_event} by { value_event}')


# -----------------------------------------------------------------

# 3 cancel
def cancel_reservation(specification, event_data):
    full_tables(specification, event_data)
    res = input('enter number of table for cancel reservation: ')
    for key_event, value_event in event_data.items():
        if str(res) == str(key_event):
            value_event.remove()
            print('work')

    print('new information')
    full_tables(specification, event_data)

# ---------------------------------------------------

def read_file():
    try:
        with open('event_info.txt', encoding='utf-8') as file:
            data = dict()
            try:
                for value in file.read().split('\n'):
                    k, v = value.split('=')
                    data[int(k)] = v
            except ValueError:
                print('file empty')
            finally:
                return data
    except FileNotFoundError:
        print('file not founded')
        with open('event_info.txt', 'w',encoding='utf-8') as file:
            file.write('')


def write_file(specification, event_data):
   pass



def menu_validation(number):
    if 0 <= number <= 5:
        return True
    return False


def free_tables(specification, event_data):
    # -----------    variant 1  -------------:
    # print(specification, event_data, sep='\n\n')
    for key, value in specification.items():
        print(f'for {key} person available tables number: ', end='')
        for key_event, value_event in event_data.items():
            if str(key_event) in value:
                value.remove(str(key_event))
        print(f'{", ".join(value)}')

    # -------------   variant 2   ------------------
    # all_tables = []
    # for value in specification.values():
    #     for table_number in value:
    #         all_tables.append(table_number)
    # all_tables.sort()
    # # print(all_tables)
    # for table in all_tables:
    #     if table not in event_data.keys():
    #         print(f'free tables : {table}')


def book_table(file_name, *args, **kwargs):
    pass


event_data = read_file()
print(event_data)
spec_read_good = False
try:
    with open('place_specification.txt', encoding='utf-8') as file:
        spec = dict()
        for value in file.read().split('\n\n'):
            k, v = value.split()
            #spec[int(k)] = tuple([int(num) for num in v.split(',')])
            spec[int(k)] = v.split(',')
        spec_read_good = True
        # print(spec)
except FileNotFoundError:
    print('cant find place_specification file ')


while spec_read_good:
    try:
        menu_choice = int(input('\t*** rezerv ***\n1 - book\n2 - update\n3 - canceled\n\n'
                                '\t*** info ***\n4 - available\n5 - full\n0 - Exit\n'
                                'Enter your choice:'))
    except ValueError:
        print('enter a number!')
        continue
    if menu_validation(menu_choice):
        if menu_choice == 4:
            free_tables(specification=spec, event_data=event_data)
        elif menu_choice == 1:
            book_tables(specification=spec, event_data=event_data)
        elif menu_choice == 5:
            full_tables(specification=spec, event_data=event_data)
        elif menu_choice == 3:
            cancel_reservation(specification=spec, event_data=event_data
                               )
        elif menu_choice == 0:
            print('have a nice day')
            break
        else:
            print('please enter correct number')