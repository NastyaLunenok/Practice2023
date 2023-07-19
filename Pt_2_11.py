print("Введите отрезок целых чисел [a,b]")
a, b = map(int, input().split())
summ = 0
for i in range(a, b + 1):
    summ += i
print("Сумма всех целых чисел от a до b:", summ)
