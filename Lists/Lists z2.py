num = int(input("Введите последовательность чисел: "))
a = []
a2 = []
while num != 0:
    a.append(num)
    num = int(input())
for i in a:
    if i not in a2:
        a2.append(i)
# a2 = list(set(a))
print(sorted(a2, reverse=True))