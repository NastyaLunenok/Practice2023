print("Введите длину списка чисел")
n = int(input())
print("Введите", n, "чисел")
number = []
for i in range(n):
    number.append(int(input()))
average_value = lambda x: sum(x) / len(x)
print(average_value(number))
