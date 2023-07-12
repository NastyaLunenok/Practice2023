import itertools
n=int(input("Введите длину списка: "))
listt=[]
print("Введите значения элементов списка:")
for i in range(n):
    listt.append(input())

print(list(itertools.permutations(listt)))
