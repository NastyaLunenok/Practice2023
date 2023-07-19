print("Введите число от 10 до 20:")
flag = False
while not (flag):
    number = int(input())
    if number < 10:
        print("Число меньше требуемого диапазона. Введите число ещё раз:")
        flag = False
    elif number > 20:
        print("Число больше требуемого диапазона. Введите число ещё раз:")
        flag = False
    else:
        flag = True
        print("Спасибо")
