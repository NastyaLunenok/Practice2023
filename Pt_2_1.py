import random
fl=False
program_number=random.randint(1,5)
while not(fl):
    print("Выберите один цвет(введите соответствующее число)")
    print(" 1. Красный \n 2. Зелёный \n 3. Голубой \n 4. Жёлтый \n 5. Фиолетовый")
    flag=False
    while not(flag):
        number=int(input())
        if number<1 or number>5:
            print("Данному номеру не соответствует ни один из цветов. Введите номер ещё раз")
        else:
            flag=True
    if number==program_number:
        print("Отлично!")
        fl=True
    else:
        print("Цвета не совпали. Попробуйте ещё раз.")
        if program_number==1:
            print("Подсказка: Этот цвет запрещает движение на дороге")
        if program_number==2:
            print("Подсказка: Какой цвет имеет трава?")
        if program_number==3:
            print("Подсказка: Какого цвета небо?")
        if program_number==4:
            print("Подсказка: Цвет одуванчиков")
        if program_number==5:
            print("Подсказка: Седьмой цвет радуги")
        
