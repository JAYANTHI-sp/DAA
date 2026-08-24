# DAA practical1

SUMMARY:

Sorting algorithms arrange data in ascending or descending order. Different sorting methods have different approaches and performance.
Bubble Sort is Simple but slow for large datasets.
Selection Sort is Selects the smallest/largest element and places it in the correct position.
Insertion Sort inserts each element into its correct position,good for small or nearly sorted data.
Merge Sort Uses divide-and-conquer and provides O(n log n) performance.
Quick Sort is Fast and efficient in most cases, with O(n log n) average time and
Overall The best sorting method depends on data size, speed requirements, memory, and whether the data is already partially sorted.


CONCLUSION:

Sorting algorithms are used to arrange data in a specific order, making searching and data processing easier.
Different methods such as Bubble Sort, Selection Sort, Insertion Sort, Merge Sort and Quick Sort have different advantages and limitations.
Simple algorithms like Bubble, Selection, and Insertion Sort are easy to understand but are less efficient for large datasets.
Merge Sort provide better performance with O(n log n) time complexity.
Quick Sort is usually very fast in practice, although its worst-case complexity can be O(n²).
The choice of sorting algorithm depends on the size of the data, required speed, memory usage, and problem requirements.




# Practical2

SUMMARY:

In this practical,Linear Search and Binary Search algorithms were implemented and their execution times were analyzed. Linear Search checks each element sequentially until the required element is found or the list ends. Binary Search works on a sorted list and repeatedly divides the search range into two halves, making it more efficient for large datasets. The execution time of both algorithms was measured for user-provided input. Linear Search has a worst-case time complexity of O(n), while Binary Search has a worst-case time complexity of O(log n).

 
CONCLUSION:

The practical demonstrates that Binary Search is more efficient than Linear Search when the input data is sorted. Linear Search is simple and can be used on both sorted and unsorted data, whereas Binary Search requires sorted data but significantly reduces the number of comparisons. The time analysis shows that Binary Search performs better as the input size increases. Therefore, the choice of searching algorithm depends on the nature and size of the dataset.


# Practical3

SUMMARY:

In this practical, the Max-Heap Sort algorithm was implemented to sort a given set of elements. The algorithm first constructs a max heap, where the largest element is placed at the root. The root element is then exchanged with the last element, and the heap is adjusted repeatedly until all elements are sorted. The execution time can be measured for user-provided input to analyze the performance of the algorithm. Max-Heap Sort has a best-case, average-case, and worst-case time complexity of O(n log n).

CONCLUSION:

The practical demonstrates that Max-Heap Sort is an efficient comparison-based sorting algorithm with consistent O(n log n) time complexity. It does not require additional memory proportional to the input because it performs sorting in-place. Although Heap Sort may not be as fast as some practical implementations of Quick Sort, its guaranteed worst-case performance makes it useful when predictable execution time is important. Thus, Max-Heap Sort is suitable for efficiently sorting large datasets.

# Practical4

SUMMARY:

The factorial of a number was implemented using both iterative and recursive approaches. The program accepts a number from the user and calculates its factorial using both methods. The execution time of each method is measured using Python's time.perf_counter() function. Both approaches have O(n) time complexity, but they differ in space requirements. The iterative method requires O(1) space, whereas the recursive method requires O(n) space because of recursive function calls.

CONCLUSION:

The factorial program was successfully implemented using iterative and recursive methods. Both methods produce the same factorial result and have O(n) time complexity. However, the iterative method is more memory-efficient because it uses O(1) space, while the recursive method uses O(n) stack space. Execution-time analysis helps compare their practical performance. Thus, the iterative method is generally preferable when memory efficiency is important



# Practical7

SUMMARY:

The Making Change Problem was implemented using the Dynamic Programming technique. The program accepts coin denominations and the target amount as user input and determines the minimum number of coins required to make the given amount. Dynamic Programming avoids repeated calculations by storing previously computed results in a table. The execution time of the program is measured using Python's time.perf_counter() function. The algorithm has a time complexity of O(n × A) and a space complexity of O(A), where n is the number of coin denominations and A is the target amount.

CONCLUSION:

The Making Change Problem was successfully solved using Dynamic Programming. The approach efficiently finds the minimum number of coins by breaking the problem into smaller subproblems and storing their solutions. Compared with a simple recursive approach, Dynamic Programming reduces unnecessary repeated computations. The execution-time analysis helps evaluate the practical performance of the algorithm. Overall, Dynamic Programming provides an efficient solution for the minimum coin change problem with O(n × A) time complexity and O(A) space complexity.





