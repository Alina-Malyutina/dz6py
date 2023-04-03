from random import randint
list_1 = [randint(-100, 101) for i in range(15)]
mini = int(input('Enter minimum number: '))
maxi = int(input('Enter maximum number: '))
for i in range(len(list_1)):
    if mini <= list_1[i] <= maxi:
        print(i, end = ', ')