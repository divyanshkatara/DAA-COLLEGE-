def can_allocate(pages, students, limit):
    count = 1
    total = 0

    for p in pages:
        if total + p > limit:
            count += 1
            total = p
        else:
            total += p

    return count <= students


def min_pages(pages, students):
    low = max(pages)
    high = sum(pages)

    while low < high:
        mid = (low + high) // 2

        if can_allocate(pages, students, mid):
            high = mid
        else:
            low = mid + 1

    return low


pages = [12, 34, 67, 90]

print("Minimum maximum pages:", min_pages(pages, 2))
