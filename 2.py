import random

def ListCreation(length):
    list1 = []
    for i in range(length):
        list1.append(random.randint(0, 10))
    print(list1)
    return list1

first_list_len = int(input('input 1 LL: '))
first_list = ListCreation(first_list_len)
count = 0

for i in range(1, first_list_len-1):
    if first_list[i] > first_list[i-1] and first_list[i] > first_list[i+1]:
        count +=1
print(count)