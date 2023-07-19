print("Введите 3 числа")
mas = []
for i in range(3):
    mas.append(int(input()))
mas.sort(reverse=True)
print("Наибольшее число:", max(mas))
print("Числа в порядке убывания:", mas)
