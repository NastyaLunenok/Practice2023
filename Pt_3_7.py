print("Введите строку")
consonants = ["б", "в", "г", "д", "ж", "з", "й", "к", "л", "м", "н",
              "п", "р", "с", "т", "ф", "х", "ц", "ч", "ш", "щ"]
vowels = ["а", "е", "ё", "и", "о", "у", "ы", "э", "ю", "я"]
string = input().lower()
dic = {}
for i in range(len(string)):
    if string[i] in dic.keys():
        pass
    else:
        if string[i] in consonants:
            dic[string[i]] = False
        if string[i] in vowels:
            dic[string[i]] = True
print(dic) 
