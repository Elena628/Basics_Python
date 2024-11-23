num = int(input("Введите последовательность чисел: "))
a = []
while num != 0:
    a.append(num)
    num = int(input())
print(f"Количество всех элементов: {len(a)}", f"Количество единиц: {a.count(1)}",
      f"Индекс первой единицы: {a.index(1)}", sep="\n")
