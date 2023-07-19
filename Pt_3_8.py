alph = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
dic = {}
i = 1
for letter in alph:
    dic[letter] = i
    i += 1

print(dic)
