arr = [10, 7, 6, 3, 14, 5, 9, 100, 6, 2]


def search(arr, search):
    for i in range(len(arr)):
        if arr[i] == search:
            return i

    return -1


i = search(arr, 12)

print(i)
