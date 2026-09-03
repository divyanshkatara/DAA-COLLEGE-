n = int(input("Enter number of elements: "))
arr = list(map(int, input("Enter elements (0,1,2 only): ").split()))

low = 0
mid = 0
high = n - 1

while mid <= high:
    if arr[mid] == 0:
        arr[low], arr[mid] = arr[mid], arr[low]
        low += 1
        mid += 1

    elif arr[mid] == 1:
        mid += 1

    else:
        arr[mid], arr[high] = arr[high], arr[mid]
        high -= 1

print("Sorted Array:", arr)
