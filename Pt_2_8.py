print("Введите число")
n= int(input())
for x in range(1, n+2):
    if x**2>n:
        print("Число:", x, "\nКвадрат числа:", x**2)
        break
