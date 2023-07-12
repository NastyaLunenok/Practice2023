number= int(input())
digits=list(map(int,str(number)))
summ=0
for i in range(len(digits)):
    summ+=digits[i]**(len(digits))
if summ==number:
    print("Является числом Армстронга")
else:
    print("Не является числом Армстронга")
