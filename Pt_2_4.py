print("Введите в строку коэффициенты a, b, c уравнения ax^2+bx+c=0")
a, b, c = map(int, input().split())
D = b**2 - 4 * a * c
if D < 0:
    print("Корней нет")
elif D == 0:
    print("Один корень:")
    x = -b / (2 * a)
    print("x =", x)
else:
    print("Два корня:")
    x1 = (-b + D**(0.5)) / (2 * a)
    x2 = (-b - D**(0.5)) / (2 * a)
    print(" x1 =", x1, "\n", "x2 =", x2)
