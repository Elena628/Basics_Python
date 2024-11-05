num = int(input("Введите последовательность чисел: "))
max = float("-inf")
while num != 0:
    if (num > max) and ((num % 2 == 0) or (num % 3 == 0)) and (num % 10 != 8):
        max = num
    num = int(input())
if max == float("-inf"):
    print("Последовательность пустая или нет чисел удовлетворяющих условию")
else:
    print("Наибольшее число в последовательности:", max)