nums = list()
[nums.append(int(input())) for i in range(9)]
max = max(nums)
print(max)
print(nums.index(max) + 1)
