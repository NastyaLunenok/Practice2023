import random
kol_loss = 0
kol_win = 0
accounting = []
i = 0
while kol_loss != 3:
    print("Орёл или решка")
    print("Введите 0, если выбираете орла, 1 - решку")
    num = int(input())
    num_prog = random.randint(0, 1)
    if num != 0 and num != 1:
        print("Конец игры")
        break
    if num == num_prog:
        print("Вы выиграли")
        kol_win += 1
        accounting.append(1)
        i += 1
    else:
        print("Вы проиграли")
        kol_loss += 1
        accounting.append(0)
        i += 1
print("Конец игры")
print("-" * 50)
print("Количество выигрышей:", kol_win)
print("Количество проигрышей:", kol_loss)
for j in range(len(accounting)):
    if accounting[j] == 0:
        print("Раунд №", j + 1, "- проигрыш")
    else:
        print("Раунд №", j + 1, "- выигрыш")
