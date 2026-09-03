def merge(a, b):
    i = j = count = 0
    result = []

    while i < len(a) and j < len(b):

        if a[i] <= b[j]:
            result.append(a[i])
            i += 1

        else:
            result.append(b[j])
            count += len(a) - i
            j += 1

    return result + a[i:] + b[j:], count


def inversion(a):
    if len(a) <= 1:
        return a, 0

    mid = len(a) // 2

    left, x = inversion(a[:mid])
    right, y = inversion(a[mid:])

    merged, z = merge(left, right)

    return merged, x + y + z


a = [2, 4, 1, 3, 5]

print("Inversions:", inversion(a)[1])
