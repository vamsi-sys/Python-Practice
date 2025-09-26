#Write a function to find the largest number in each list from a group of lists.

def find_largest(lists):
    newList = []
    for num in lists:
        a = max(num)
        newList.append(a)
    print(newList)
        
find_largest([[1, 2, 3], [4, 5, 6], [7, 8, 9]])