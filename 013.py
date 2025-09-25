#Write a function to check if a given letter is present in a given string.

def check_letter(string, letter):
    if letter in string:
        return True
    else:
        return False
    
print(check_letter("hello", "e"))
print(check_letter("hello", "a"))