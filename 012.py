#Write a function to check if a given string is a palindrome.

def is_palindrome(s):
    s = list(s)
    s2 = s[::-1]
    if s == s2:
        return True
    else:
        return False
    
print(is_palindrome("madama"))