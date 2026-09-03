def search(a, key):
    low, high = 0, len(a) - 1

    while low <= high:
        mid = (low + high) // 2

        if a[mid] == key:
            return mid

        if a[low] <= a[mid]:

            if a[low] <= key < a[mid]:
                high = mid - 1
            else:
                low = mid + 1

        else:

            if a[mid] < key <= a[high]:
                low = mid + 1
            else:
                high = mid - 1

    return -1


a = [4, 5, 6, 7, 0, 1, 2]

print("Index:", search(a, 0))
