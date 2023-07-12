print("Введите число")
number=int(input())
even = lambda x: x % 2 == 0
if even(number):
    print("Число является четным")
else:
    print("Число является нечетным")
