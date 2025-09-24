# 2) Use map, find out the number of digits in the numbers in the given list
# input:  [189, 10, 200]
# output: [3, 2, 3]

nums = [189, 10, 200]
a = map(lambda x:len(str(x)), nums)
print (list(a))