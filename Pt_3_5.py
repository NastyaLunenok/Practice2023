lower_value = int(input("Введите нижнюю границу диапазона: "))
upper_value = int(input("Введите верхнюю границу диапазона: "))
listt = []
for number in range(lower_value, upper_value + 1):
    if number > 1:
        for i in range(2, number):
            if (number % i) == 0:
                listt.append(number)
                break

print("Cписок из чисел, которые не являются простыми", listt)
