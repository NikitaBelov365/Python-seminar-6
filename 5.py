list1 = [0, 1, 2, 3, 4, 5, 6, 7, 8]

for i in range(0,5):
    num = int(input('input int: '))
    while list1[num] == str('X') or list1[num] == str('O'):
        num = int(input('already exist, input again: '))
    list1[num] = str('X')
    if (list1[0] == str('X') and list1[1] == str('X') and list1[2] == str('X')) or (list1[3] == str('X') and list1[4] == str('X') and list1[5] == str('X')) or (list1[6] == str('X') and list1[7] == str('X') and list1[8] == str('X')) or (list1[0] == str('X') and list1[4] == str('X') and list1[8] == str('X')) or (list1[2] == str('X') and list1[4] == str('X') and list1[6] == str('X')) or (list1[0] == str('X') and list1[3] == str('X') and list1[6] == str('X')) or (list1[1] == str('X') and list1[4] == str('X') and list1[7] == str('X')) or (list1[2] == str('X') and list1[5] == str('X') and list1[9] == str('X')):
        print('X won! GC!')
        break
    while list1[i] == str('X') or list1[i] == str('O'):
        i +=1
    list1[i] = str('O')
    if (list1[0] == str('O') and list1[1] == str('O') and list1[2] == str('O')) or (list1[3] == str('O') and list1[4] == str('O') and list1[5] == str('O')) or (list1[6] == str('O') and list1[7] == str('O') and list1[8] == str('O')) or (list1[0] == str('O') and list1[4] == str('O') and list1[8] == str('O')) or (list1[2] == str('O') and list1[4] == str('O') and list1[6] == str('O')) or (list1[0] == str('O') and list1[3] == str('O') and list1[6] == str('O')) or (list1[1] == str('O') and list1[4] == str('O') and list1[7] == str('O')) or (list1[2] == str('O') and list1[5] == str('O') and list1[9] == str('O')):
        print('O won! GC!')
        break