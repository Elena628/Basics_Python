s = input("Введите строку: ")

s2 = [i for i in s if ((ord("Z") >= ord(i) >= ord("A")) or
            (ord("z") >= ord(i) >= ord("a")) or (ord("Я") >= ord(i) >= ord("А")) or
          (ord("я") >= ord(i) >= ord("а")) or
          (ord(i) == ord("Ё")) or (ord(i) == ord("ё")))]

if all(((ord("Z") >= ord(y) >= ord("A")) or (ord("Я") >= ord(y) >= ord("А")) or
                        (ord(y) == ord("Ё"))) for y in s2):
    answer = "YES"
else:
    answer = "NO"

print(answer)
