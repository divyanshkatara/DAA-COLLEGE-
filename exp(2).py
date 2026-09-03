import time

n = int(input("Enter number of elements: "))
arr = list(map(int, input("Enter elements: ").split()))

start = time.perf_counter_ns()

for i in range(1, n):
    key = arr[i]
    j = i - 1

    while j >= 0 and arr[j] > key:
        arr[j + 1] = arr[j]
        j -= 1

    arr[j + 1] = key

end = time.perf_counter_ns()

print("Sorted Array:", arr)
print("Execution time:", end - start, "ns")
