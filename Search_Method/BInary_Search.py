def binary_search(array, value, low, high):
    if high < low:
        return -1
    else:
        mid = (low+high)//2
        if array[mid] > value:
            return binary_search(array, value, low, mid)
        elif array[mid] < value:
            return binary_search(array, value, mid, high)
        else:
            return mid


res = binary_search([1, 1, 2], 1, 0, 2)
print(res)
