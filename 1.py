import random

def ListCreation(length):
    list1 = []
    for i in range(length):
        list1.append(random.randint(0, 10))
    print(list1)
    return list1

first_list_len = int(input('input 1 LL: '))
second_list_len = int(input('input 2 LL: '))
first_list = ListCreation(first_list_len)
second_list = ListCreation(second_list_len)

def Solution(first_list, second_list):
    result_list = []
    for i in range(len(first_list)):
        switcher = True
        for j in range(len(second_list)):
            if first_list[i] == second_list[j]:
                switcher = False
        if switcher:
            result_list.append(first_list[i])
    print(result_list)

Solution(first_list, second_list)