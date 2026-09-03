def union_intersection(A, B):
    i = 0
    j = 0

    union = []
    intersection = []

    while i < len(A) and j < len(B):

        if A[i] < B[j]:
            if not union or union[-1] != A[i]:
                union.append(A[i])
            i += 1

        elif A[i] > B[j]:
            if not union or union[-1] != B[j]:
                union.append(B[j])
            j += 1

        else:
            if not union or union[-1] != A[i]:
                union.append(A[i])

            if not intersection or intersection[-1] != A[i]:
                intersection.append(A[i])

            i += 1
            j += 1

    while i < len(A):
        if not union or union[-1] != A[i]:
            union.append(A[i])
        i += 1

    while j < len(B):
        if not union or union[-1] != B[j]:
            union.append(B[j])
        j += 1

    return union, intersection


A = [1, 2, 4, 5]
B = [2, 4, 6]

union, intersection = union_intersection(A, B)

print("Union:", union)
print("Intersection:", intersection)
