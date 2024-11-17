num = int(input("Введите последовательность чисел: "))
a = []
while num != 0:
    a.append(num)
    num = int(input())
a2 = list(set(a))
print(sorted(a2, reverse=True))