i = int(input("Введите числа: "))
max = i
while i != 0:
    if i > max:
        max = i
    i = int(input())
print("Наибольшее число в последовательности:", max)