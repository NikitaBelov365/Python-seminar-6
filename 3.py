import random

def ListCreation(length):
    list1 = []
    for i in range(length):
        list1.append(random.randint(0, 10))
    print(list1)
    return list1

first_list_len = int(input('input 1 LL: '))
first_list = ListCreation(first_list_len)
counter = 0

for i in range(len(first_list)-1-counter):
    print("i= ", i)
    for j in range(i+1, len(first_list)-counter):
        print("ij = ", i, j)
        print(first_list[i], first_list[j])
        if first_list[i] == first_list[j]:
            first_list.pop(j)
            first_list.pop(i)
            print(first_list)
            counter += 2
            i = 0
            break

print("counter = ", counter)