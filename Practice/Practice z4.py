poww = int(input("Введите степень: "))
amount = int(input("Введите количество строк: "))
a = [int(input(f"Введите число {i}: ")) for i in range(1, amount + 1)]
# a2 = [n ** poww for n in a]
print([n ** poww for n in a])
