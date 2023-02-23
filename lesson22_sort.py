# -----------   S O R T I N G    -----------

# 1 # bubble sorting
from random import randint

def generate_lst():
    l = []
    for _ in range(21):
        #count = 0
        while True:
            rand_num = randint(-10, 10)
            #count += 1
            if rand_num not in l:
                l.append(rand_num)
                break
        #print(count)
    return l

lst = generate_lst()
# # lst = [randint(-10, 10) for _ in range(21)]
# print(generate_lst())
# print(sorted(generate_lst()))

# ------------------------------------------------------------------

# # 2 bubble sort
# def bubble_sort(lst):
#     for i in range(len(lst)):
#         for j in range(1, len(lst) - i):
#             if lst[j - 1] > lst[j]:
#                 lst[j - 1], lst[j] = lst[j], lst[j - 1]
#     return lst
#
#
# data = generate_lst()
# rand_data = [randint(-10, 10) for _ in range(21)]
#
# print(data)
# # print(rand_data)
# res = bubble_sort(data)
# print(res)

# -------------------------------------------------

# # 3 clear
# def decorator(func):
#     lst = []
#
#     def wrapper(*args,clear=False, **kwargs):
#         print(kwargs,args)
#
#         if clear:
#             lst.clear()
#
#         lst.append(func(*args, **kwargs))
#         return lst
#     return wrapper
#
#
# @decorator
# def a(num):
#     return num
#
#
# print(a(3))
# print(a(2))
# print(a(1, clear=True))

#print(a(4))



# 4 selection sort
def selection_sort(lst):
    for i in range(len(lst) - 1):
        min = i
        for j in range(i + 1, len(lst)):
            if lst[j] < lst[min]:
                min = j
        lst[i],lst[min] = lst[min], lst[i]
    return lst


data = generate_lst()
rand_data = [randint(-10, 10) for _ in range(21)]
res = selection_sort(data)
res1 = selection_sort(rand_data)
print(res)
print(res1)
