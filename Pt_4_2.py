def search(s, low, high, palindromes):
    while low >= 0 and high < len(s) and s[low] == s[high]:
        palindromes.add(s[low: high + 1])
        low = low - 1
        high = high + 1
 
def PalindromicSubstrings(s):
    palindromes = set()
    for i in range(len(s)):
        search(s, i, i, palindromes) #поиск палиндромов нечетной длины
        search(s, i, i + 1, palindromes) #поиск палиндромов четной длины
    print(palindromes, end='')

s = input("Введите строку: ")
PalindromicSubstrings(s)
