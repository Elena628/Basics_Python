num = int(input("Введите последовательность чисел: "))
max = 1
while num != 0:
    if (num > max) and ((num % 2 == 0) or (num % 3 == 0)) and (num % 10 != 8):
        max = num
    num = int(input())
print("Наибольшее число в последовательности:", max)