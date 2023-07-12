digit=int(input("Введите число: "))
num=list(str(abs(digit)))
if digit>0:
    num.sort(reverse=True)
    print("Наибольшее число:", "".join(num))
    
else:
    num.sort()
    num_int=int("".join(num))*(-1)
    print("Наибольшее число:", num_int)
