amount = int(input("Введите количество рядов: "))
for i in range(1, amount + 2):
    s = i * "*"
    print(s)
for i in range(amount, 0, -1):
    s = i * "*"
    print(s)