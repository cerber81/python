
a = [5, 1, 5, 8, 9]

print('Введите 1 число')
a[0] = int(input())

print('Введите 2 число')
a[1] = int(input())

print('Введите 3 число')
a[2] = int(input())

print('Введите 4 число')
a[3] = int(input())

print('Введите 5 число')
a[4] = int(input())

b = 0
c = 1
max = a[0]
while b <= 3:
    if (max < a[c]):
        max = a[c]
        c += 1
    elif (max > a[c]):
        c += 1
    b += 1


print(f"Мах знач : {max}")
