n = int(input("Enter number of elements: "))
arr = list(map(int, input("Enter elements: ").split()))

# Find candidate
candidate = None
count = 0

for num in arr:
    if count == 0:
        candidate = num
        count = 1
    elif num == candidate:
        count += 1
    else:
        count -= 1

# Verify candidate
count = 0

for num in arr:
    if num == candidate:
        count += 1

if count > n // 2:
    print("Majority element is:", candidate)
else:
    print("No majority element")
