
import time

def insertion_sort(arr):

    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        while j >= 0 and arr[j] > key:
            arr[j+1] = arr[j]
            j -= 1

        arr[j+1] = key

numbers = list(map(int, input("Enter numbers: ").split()))

start = time.perf_counter()
insertion_sort(numbers)
end = time.perf_counter()

print("Sorted List:", numbers)
print("Execution Time:", end - start, "seconds")

print("\nTime Complexity")
print("Best   : O(n)")
print("Average: O(n²)")
print("Worst  : O(n²)")
