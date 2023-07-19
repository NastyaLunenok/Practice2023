TV_programs = [" Орёл и решка", "Голос", "Танцы", "Импровизвция"]
print(*[element + '\n' for element in TV_programs])
print("Введите название передачи")
title = input()
print("Введите позицию передачи в списке")
position = int(input())
TV_programs.insert(position - 1, title)
print(*[element + '\n' for element in TV_programs])
