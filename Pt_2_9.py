print("Введите натуральное число, не содержащее одинаковых цифр")
number = int(input())
digits = list(map(int, str(number)))
max_value = max(digits)
max_index_start = digits.index(max_value)
print("Максимальная цифра:", max_value)
print("Порядковый номер максимальной цифры, считая от начала:",
      max_index_start + 1)
print("Порядковый номер максимальной цифры, считая от конца:",
      len(digits) - max_index_start)
