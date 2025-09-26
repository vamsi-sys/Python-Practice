#Write a function to replace all occurrences of ':)' in a string with a smiley face emoji.

# smiley face: 😊
def replace_smiley(text):
    for let in text:
        a = text.replace(":)", "😊")
    print(a)
    
replace_smiley('Hello :) How are you :) ?')