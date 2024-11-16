def find_len(x):
    count = 0
    for n in x:
        count += 1
    return count

s = input("Введите строку: ")
s2 = input("Введите подстроку: ")
len_s = find_len(s)
len_s2 = find_len(s2)
for i in range(0, len_s - len_s2 + 1):
    if s[i : i + len_s2] == s2:
        print(i)
        break
else:
    print("Такой подстроки нет")

