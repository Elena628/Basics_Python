s = input("Введите строку: ")
for i in "0123456789":
    if i in s:
        s = s.replace(i, "")
print("Обработанная строка:", s)