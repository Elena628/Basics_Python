s = input("Введите слово: ")
i = int(input("Введите количество строк: "))
c = 1
a = []
while c <= i:
    print(f"Введите строку {c}:")
    a.append(input())
    c += 1
sum = 0
for x in a:
    sum += x.count(s)
print(f"Повторений слова '{s}': {sum}")



