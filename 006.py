#Write a function to find the most common character in a given string.


def most_common_character(s):
    emp = []   # store unique letters
    counts = []  # store counts of each letter

    for letter in s:
        if letter not in emp:
            emp.append(letter)          # add new letter
            counts.append(s.count(letter))  # count its frequency

    # find the index of the maximum count
    max_index = counts.index(max(counts))
    return emp[max_index]


print(most_common_character("hello wooorld"))
