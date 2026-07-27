
import time

def merge_sort(arr):
    if len(arr) > 1:

        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]

        merge_sort(left)
        merge_sort(right)

        i = j = k = 0

        while i < len(left) and j < len(right):

            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1

            k += 1

        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1

numbers = list(map(int, input("Enter numbers: ").split()))

start = time.perf_counter()
merge_sort(numbers)
end = time.perf_counter()

print("Sorted List:", numbers)
print("Execution Time:", end - start, "seconds")

print("\nTime Complexity")
print("Best   : O(n log n)")
print("Average: O(n log n)")
print("Worst  : O(n log n)")
