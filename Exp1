import time
import matplotlib.pyplot as plt

n = int(input("Enter the number of observations: "))
elements = []
time_ns = []

for i in range(n):
    x = int(input("Enter number of elements: "))
    y = int(input("Enter execution time (ns): "))

    elements.append(x)
    time_ns.append(y)

plt.plot(elements, time_ns, marker='o', linestyle='-')
plt.title("Insertion Sort Execution Time")
plt.xlabel("No. of elements")
plt.ylabel("Execution time (ns)")
plt.grid(True)
plt.show()
