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



# practical6

Summary:

The Matrix Chain Multiplication problem is implemented using the Dynamic Programming technique. The program accepts the number and dimensions of matrices from the user and determines the most efficient order in which the matrices should be multiplied. Instead of performing the actual matrix multiplication, it calculates the minimum number of scalar multiplications required. A dynamic programming table is used to store previously calculated results and avoid repeated calculations. The program also measures the execution time using Python's time.perf_counter() function. The time complexity of the algorithm is O(n³) and the space complexity is O(n²).


Conclusion:

The Matrix Chain Multiplication problem demonstrates how Dynamic Programming can efficiently solve an optimization problem by dividing it into smaller overlapping subproblems. The algorithm finds the optimal multiplication order while minimizing the number of scalar operations. Compared with trying all possible parenthesizations, dynamic programming significantly improves efficiency. The execution-time measurement helps analyze the practical performance of the algorithm. Thus, Matrix Chain Multiplication is a good example of applying dynamic programming to improve computational efficiency.




# practical8

summary:

The implementation of Graph Traversal using DFS and BFS demonstrates how a graph can be represented using an adjacency list and traversed using two different searching techniques. DFS (Depth First Search) visits nodes by going as deep as possible before backtracking, while BFS (Breadth First Search) visits nodes level by level using a queue.

Conclusion:

Thus, DFS and BFS graph traversal algorithms were successfully implemented and executed. The experiment helped in understanding how graphs are represented and how different searching techniques traverse the vertices.DFS explores the graph depth-wise, while BFS explores the graph level-wise. DFS generally uses recursion or a stack, whereas BFS uses a queue. Both algorithms are important fundamental graph algorithms and have applications in path finding, network analysis, connectivity checking, cycle detection, and searching problems.


# practical9

summary:

The practical focuses on the implementation of Prim’s Algorithm to find the Minimum Spanning Tree (MST) of a connected, weighted, and undirected graph. Prim’s Algorithm starts from any selected vertex and repeatedly selects the minimum-weight edge that connects a vertex already included in the MST to a vertex that is not yet included.A set of visited or selected vertices is maintained to avoid selecting the same vertex repeatedly. The process continues until all vertices are included in the MST. The algorithm ensures that no cycle is formed and produces a spanning tree with the minimum possible total edge weight.

conclusion:

Prim’s Algorithm was successfully implemented and executed to obtain the Minimum Spanning Tree of the given weighted graph. The algorithm selects the minimum-cost edge at each step while gradually connecting all vertices.The practical helped in understanding the concept of Minimum Spanning Trees, greedy algorithms, weighted graphs, and edge selection. Prim’s Algorithm is useful in applications such as network design, computer networks, electrical grids, road connections, and communication systems, where the goal is to connect all nodes with minimum total cost.



# practical10

summary:

The practical focuses on the implementation of Kruskal’s Algorithm to find the Minimum Spanning Tree (MST) of a connected, weighted, and undirected graph. Kruskal’s Algorithm follows a greedy approach by first sorting all the edges in increasing order of their weights.The algorithm then selects the smallest-weight edge and adds it to the spanning tree if it does not create a cycle. A Union-Find (Disjoint Set) data structure is used to detect cycles efficiently. This process continues until all vertices are connected and the MST contains V − 1 edges.

Conclusion:

Thus Kruskal’s Algorithm was successfully implemented and executed to obtain the Minimum Spanning Tree of the given weighted graph. The algorithm selects the edges with the lowest weights while ensuring that no cycle is formed.The practical helped in understanding greedy algorithms, weighted graphs, Minimum Spanning Trees, edge sorting, and cycle detection using Union-Find. Kruskal’s Algorithm is useful in applications such as network design, communication networks, road networks, and connecting systems at minimum cost.
