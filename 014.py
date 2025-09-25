#Write a function to check if a given number is a palindrome or not.
def is_palindrome(n):
    num_str = str(n)
    num_str = num_str[::-1]
    if num_str == str(n):
        return True
    else:
        return False
    
print(is_palindrome(122))