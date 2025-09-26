def outer_function(x):
    def inner_function(y):
        return x + y  # inner function can use outer variable
    return inner_function(10)

print(outer_function(5))  # Output: 15
