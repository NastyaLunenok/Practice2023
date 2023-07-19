print("Введите в строку ваше имя и возраст:")
name, age = map(str, input().split())
if (1 <= (int(age) % 10) <= 4) and (int(age) < 10 or int(age) > 20):
    string = "Привет, " + name + "! Тебе уже " + age + " года."
else:
    string = "Привет, " + name + "! Тебе уже " + age + " лет."
print(string)
