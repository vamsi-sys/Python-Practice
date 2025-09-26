#1) Use map, find out square root of all the numbers in the list

# input:  [64, 16, 9]
# output: [8, 4, 3]

def sqr(n):
    return list(map(lambda x: int(x ** 0.5), n))

print(sqr([64, 16, 9]))
