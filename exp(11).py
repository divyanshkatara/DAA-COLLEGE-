import random


def quick_sort(a):
    if len(a) <= 1:
        return a

    pivot = random.choice(a)

    left = [x for x in a if x < pivot]
    middle = [x for x in a if x == pivot]
    right = [x for x in a if x > pivot]

    return quick_sort(left) + middle + quick_sort(right)


a = [5, 2, 8, 1, 3, 7]

print("Sorted:", quick_sort(a))
