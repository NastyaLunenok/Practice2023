lower_value = int(input("Введите нижнюю границу диапазона: ")) 
upper_value = int(input("Введите верхнюю границу диапазона: "))
 
print("Простые числа в заданном диапазоне: ") 
for number in range(lower_value, upper_value + 1): 
    if number > 1: 
        for i in range(2, number): 
            if(number % i) == 0: 
                break 
        else: 
            print(number)
