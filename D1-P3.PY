# 3. Fibonacci Series 
# o Input: Number of terms. 
# o Output: Print the Fibonacci series up to the given number of terms. 
# o Example: For input 6 → Output: 0 1 1 2 3 5
# program:
def fibonacci(n):
    a, b = 0, 1
    for i in range(n):
        print(a, end=" ")
        a, b = b, a + b

fibonacci(6)
