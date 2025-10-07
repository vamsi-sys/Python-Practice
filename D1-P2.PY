# 2. Factorial in Expression Format 
# o Input: A number from the user. 
# o Output: Display the factorial in an expression format. 
# o Example: For input 5 → Output: 5 x 4 x 3 x 2 x 1 = 120 
# program:
def fac(n):
    a = 1
    for i in range(n,1,-1):
        print(i,end = " ")
        a = a * i
    print()
    print(f"The Factorial of {n} is {a}")
        
fac(3)
