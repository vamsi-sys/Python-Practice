# 1. Prime Number Check 
# o Input: A number from the user. 
# o Output: Print "Prime" if the number is prime, otherwise "Not a Prime".
# program:
def prime(n):
    if n > 1:
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return "Not a prime"
        return "prime"
    else:
        return "Not a prime"

print(prime(2))
