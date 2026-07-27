
import time

def bubble_sort(arr):
    n = len(arr)

    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

numbers = list(map(int, input("Enter numbers: ").split()))

start = time.perf_counter()
bubble_sort(numbers)
end = time.perf_counter()

print("Sorted List:", numbers)
print("Execution Time:", end - start, "seconds")

print("\nTime Complexity")
print("Best   : O(n)")
print("Average: O(n²)")
print("Worst  : O(n²)")
