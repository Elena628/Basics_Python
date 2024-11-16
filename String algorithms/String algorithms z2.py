s = input("Введите строку: ")
if all((ord("Z") >= ord(i) >= ord("A")) or (ord("z") >= ord(i) >= ord("a")) for i in s):
    answer = "YES"
else:
    answer = "NO"
print(answer)