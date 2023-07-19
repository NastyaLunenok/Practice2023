flag = True
summ = 0
print("Программа считает сумму отрицательных чисел. Вводите числа")
while flag:
    number = int(input())
    if number < 0:
        summ += number
    else:
        flag = False
print("Сумма отрицательных чисел:", summ)
