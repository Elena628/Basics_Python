num = int(input("Введите последовательность чисел: "))
a = []
while num != 0:
    a.append(num)
    num = int(input())
print(sorted(a, key=abs))
