
import time

def quick_sort(arr):

    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr)//2]

    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    return left + middle + right

numbers = list(map(int, input("Enter numbers: ").split()))

start = time.perf_counter()
sorted_list = quick_sort(numbers)
end = time.perf_counter()

print("Sorted List:", sorted_list)
print("Execution Time:", end - start, "seconds")

print("\nTime Complexity")
print("Best   : O(n log n)")
print("Average: O(n log n)")
print("Worst  : O(n²)")
