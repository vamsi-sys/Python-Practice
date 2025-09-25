#Write a function to find the first letter in a string that occurs only once.

def single_occurrence(s):
    null = []
    null2 = []
    for i  in s:
        if i not in null:
            null.append(i)
    for j in null:
        if s.count(j) == 1:
            null2.append(j)
    print(null2[0])
 
single_occurrence("Hello World")