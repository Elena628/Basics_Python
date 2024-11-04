num = int(input("Введите число: "))
min_del = 2
if num < 2:
    print("Введено неправильное число")
else:
    while num % min_del != 0:
        min_del += 1
print(f"Наименьший делитель {num} = {min_del}")
