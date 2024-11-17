num = int(input("Введите последовательность чисел: "))
a = []
while num != 0:
    a.append(num * num)
    num = int(input())
print(a)

