nums = []
i = int(input("Введите последовательность: "))
nums.append(i)
c = 0
while i != 0:
    i = int(input())
    nums.append(i)
for i in range(1, len(nums)):
    if nums[i] > nums[i - 1]:
        c += 1
print("Количество элементов, которые больше предыдущего:", c)
