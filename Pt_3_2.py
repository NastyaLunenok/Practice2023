from functools import reduce

print("Введите число:")
flag = False
while not (flag):
    n = int(input())
    if n < 0:
        print("Ошибка ввода. Введите положительное число:")
    else:
        flag = True

listt = [1, 1]
while listt[1] <= n:
    print(listt[1])
    x = reduce(lambda x, y: x + y, listt)
    listt[0] = listt[1]
    listt[1] = x
