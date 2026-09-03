def median(a, b):
    arr = sorted(a + b)
    n = len(arr)

    if n % 2 == 0:
        return (arr[n // 2 - 1] + arr[n // 2]) / 2
    else:
        return arr[n // 2]


a = [1, 3, 5]
b = [2, 4, 6]

print("Median:", median(a, b))
