arr = [10, 7, 6, 3, 14, 100, 9, 100, 6, 2]


def count(arr, search):
    count = 0

    for i in arr:
        count = count + 1 if i == search else count

    return count


i = count(arr, 100)

print(i)
