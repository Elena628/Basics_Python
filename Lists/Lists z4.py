d = int(input("Введите длину строки: "))
i = int(input("Введите количество строк: "))
c = 1
a = []
while c <= i:
    print(f"Введите строку {c}:")
    a.append(input())
    c += 1
for x in range(i):
    if len(a[x]) > d:
        a[x] = a[x][0:d - 3] + "..."
for y in a:
    print(y)



