# 3. Perfect Number Check 
# o A perfect number is a number equal to the sum of its proper divisors (excluding 
# itself). 
# o Example: 6 → Divisors: 1, 2, 3 → Sum = 6 → Output: "Perfect Number"

def pr(n):
    su = 0
    for i in range(1,n):
        if n % i == 0:
            su += i
    if su == n:
        print("perfect number")
    else:
        print("not a perfect number")
            
pr(6)