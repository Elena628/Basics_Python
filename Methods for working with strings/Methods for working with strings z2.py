s = input()
print(s[ : s.find("е")] + s[s.rfind("е") + 1 : ])