def SumDiv(num):
    div = num-1
    summ = 0
    while div != 0:
        if num%div == 0:
            summ += div
        div -= 1
    return summ

def Enum(num):
    dict1 = {}
    for i in range(1, num+1):
        dict1[i] = (SumDiv(i))
    return dict1

def Solution(dict1):
    list1 = []
    for key in dict1:
        for item in dict1:
            if key == item:
                break
            elif key == dict1[item]:
                if item == dict1[key]:
                    list1.append((key, item))
    return list1

dict1 = Enum(3000)

print(Solution(dict1))