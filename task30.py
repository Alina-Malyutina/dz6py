a1 = int(input('Enter first number of progression: '))
d = int(input('Enter difference: '))
n = int(input('Enter quantity of numbers: '))
progress = [a1 + (i - 1) * d for i in range(1, n + 1)]
print(progress)