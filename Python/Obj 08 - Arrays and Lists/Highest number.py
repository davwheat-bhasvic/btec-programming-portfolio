numbers_list = [4, 6, 2, 5, 8, 2, 1, 5, 8, 3, 9]

highest = numbers_list[0]

# Skip index 0 -- this is done to avoid comparing the first number to itself
for i in range(1, len(numbers_list)):
    if highest < numbers_list[i]:
        highest = numbers_list[i]

print(f"Highest number is {highest}")
