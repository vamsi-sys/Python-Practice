from functools import reduce

nums = [1, 2, 3, 4, 5]

sum_all = reduce(lambda a, b: a + b, nums)
print(sum_all)  # 15
