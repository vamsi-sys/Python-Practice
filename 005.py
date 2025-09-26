#Write a function to replace all vowels in a string with a specified character.

def replace_vowels(string, char):
    for vowel in "aeiouAEIOU":
        string = string.replace(vowel, char)
    print(string)

replace_vowels('hello world', 'x')