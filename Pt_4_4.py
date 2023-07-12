def sum_combinations(numbers, goal, combination=[]):
    s = sum(combination)
    
    # проверяем, набрана ли необходимая сумма
    if s == goal:
        print(combination)

    #при достижении необходимого числа выходим из функции
    if s >= goal:
        return 

    for i in range(len(numbers)):
        n = numbers[i]
        remaining = numbers[i + 1:]
        sum_combinations(remaining, goal, combination + [n])

n=int(input("Введите длину списка чисел: "))
print("Введите элементы списка:")
listt=[]
for i in range(n):
    listt.append(int(input()))
num=int(input("Введите число: "))
sum_combinations(listt, num)
