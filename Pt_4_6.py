alphabet = 'abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz'
string = input("Введите строку: ")
new_string = ''

for letter in string:
    index_letter = alphabet.index(letter)
    new_index_letter = index_letter + 13
    if letter in alphabet:
        new_string += alphabet[new_index_letter]

print(new_string)
