print("Введите строку")
string = input().lower()
dic = {}
for i in range(len(string)):
    if string[i] != ' ':
        if string[i] in dic.keys():
            dic[string[i]] += 1
        else:
            dic[string[i]] = 1

print(dic)
