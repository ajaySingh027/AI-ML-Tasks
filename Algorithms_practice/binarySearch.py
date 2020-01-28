def binary_search(list, item):
    low = 0
    high = len(list) - 1

    while low <= high:
        mid = int((low + high) / 2)
        # mid is rounded down by Python automatically if (low + high) isn’t an even number.
        guess = list[mid]

        if guess == item:
            return mid
        if guess > item:
            high = mid - 1
        else:
            low = mid + 1
    return None

mylist = [1, 2, 5, 7, 8, 9, 11, 13, 14]

print(binary_search(mylist, 5))
