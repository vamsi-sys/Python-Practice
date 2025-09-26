nums = [2, 4, 6, 8]

print(any(n % 2 != 0 for n in nums))  # False → no odd numbers
print(all(n % 2 == 0 for n in nums))  # True  → all even
