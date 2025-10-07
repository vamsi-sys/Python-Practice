# Part A – Programming Tasks 
# Write Python programs for the following: 
# 1. Reverse a Number (Without Methods or Slicing) 
# o Input: A number. 
# o Output: Reverse of the number. 
# o Example: Input 1234 → Output: 4321 
# program:
def rev(n):
    rev_num = 0
    while n > 0:
        digit = n % 10          # get last digit
        rev_num = rev_num * 10 + digit  # add it to reversed number
        n = n // 10             # remove last digit
    print(rev_num)

# Example
rev(1234)   # Output: 4321
