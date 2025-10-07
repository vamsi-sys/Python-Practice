# 2. Fibonacci Series (with Examples) 
# o Input: Number of terms. 
# o Output: Print the Fibonacci series up to given number of terms. 
# o Example 1: Input 5 → Output: 0 1 1 2 3 5 
# o Example 2: Input 3 → Output: 0 1 1 2 3 
# program:

def fibonacci_until_match(n):
    a, b = 0, 1
    while True:
        print(a, end=' ')
        if a == n:
            break
        a, b = b, a + b

fibonacci_until_match(5)