
import time

def selection_sort(arr):
    n = len(arr)

    for i in range(n):
        min_index = i

        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j

        arr[i], arr[min_index] = arr[min_index], arr[i]

numbers = list(map(int, input("Enter numbers: ").split()))

start = time.perf_counter()
selection_sort(numbers)
end = time.perf_counter()

print("Sorted List:", numbers)
print("Execution Time:", end - start, "seconds")

print("\nTime Complexity")
print("Best   : O(n²)")
print("Average: O(n²)")
print("Worst  : O(n²)")
