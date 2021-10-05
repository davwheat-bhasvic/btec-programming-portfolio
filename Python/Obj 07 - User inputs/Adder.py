def isInt(x):
    try:
        int(x)
        return True
    except ValueError:
        return False


highest = 0
total = 0
count = 0

while True:
    inp = input("Enter a number: ")

    if isInt(inp):
        num = int(inp)

        count += 1
        total += num

        if num > highest:
            highest = num
    else:
        break

print(f"Total: {total}")
print(f"  Max: {highest}")
print(f"  Avg: {total / count}")