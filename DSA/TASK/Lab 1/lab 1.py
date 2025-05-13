# task 1

import random
import time
import matplotlib.pyplot as plt

# 1. Sorting algorithms

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]

        merge_sort(L)
        merge_sort(R)

        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[0]
    left = [x for x in arr[1:] if x <= pivot]
    right = [x for x in arr[1:] if x > pivot]
    return quick_sort(left) + [pivot] + quick_sort(right)

# 2. Generate random list
random_list = [random.randint(0, 10000) for _ in range(1000)]

# 3. Measure execution times
execution_times = {}

# Bubble Sort
arr_bubble = random_list.copy()
start = time.time()
bubble_sort(arr_bubble)
end = time.time()
execution_times["Bubble Sort"] = end - start

# Merge Sort
arr_merge = random_list.copy()
start = time.time()
merge_sort(arr_merge)
end = time.time()
execution_times["Merge Sort"] = end - start

# Quick Sort
arr_quick = random_list.copy()
start = time.time()
arr_quick = quick_sort(arr_quick)
end = time.time()
execution_times["Quick Sort"] = end - start

# 4. Display execution times
print("Execution Times (in seconds):")
for algo, exec_time in execution_times.items():
    print(f"{algo}: {exec_time:.6f}")

# 5. Plotting the execution times
algorithms = list(execution_times.keys())
times = list(execution_times.values())

plt.figure(figsize=(10, 6))
plt.bar(algorithms, times, color=['red', 'green', 'blue'])
plt.title("Execution Time Comparison of Sorting Algorithms")
plt.xlabel("Sorting Algorithm")
plt.ylabel("Execution Time (seconds)")
plt.grid(axis='y')
plt.show()


# task 2
import time
from functools import lru_cache

# 1. Recursive Approach (Naive)
def fib_recursive(n):
    if n <= 1:
        return n
    return fib_recursive(n - 1) + fib_recursive(n - 2)

# 2. Iterative Approach
def fib_iterative(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a

# 3. Optimized Recursive Approach using Memoization
@lru_cache(maxsize=None)
def fib_memoized(n):
    if n <= 1:
        return n
    return fib_memoized(n - 1) + fib_memoized(n - 2)

# List of test values
test_values = [10, 20, 30, 40]

# Dictionary to store results
results = {"Recursive": [], "Iterative": [], "Memoized": []}

# 4. Measure execution time for each method and each n
for n in test_values:
    # Recursive
    start = time.time()
    fib_recursive(n)
    end = time.time()
    results["Recursive"].append(end - start)

    # Iterative
    start = time.time()
    fib_iterative(n)
    end = time.time()
    results["Iterative"].append(end - start)

    # Memoized Recursive
    start = time.time()
    fib_memoized(n)
    end = time.time()
    results["Memoized"].append(end - start)

# 5. Display results
print("Execution Time (in seconds):")
print(f"{'n':>5} | {'Recursive':>10} | {'Iterative':>10} | {'Memoized':>10}")
print("-" * 45)
for i, n in enumerate(test_values):
    print(f"{n:>5} | {results['Recursive'][i]:>10.6f} | {results['Iterative'][i]:>10.6f} | {results['Memoized'][i]:>10.6f}")

# task 3

import matplotlib.pyplot as plt
import numpy as np

# 1. Time complexity functions
def O_1(n): return np.ones_like(n)
def O_log_n(n): return np.log2(n)
def O_n(n): return n
def O_n_log_n(n): return n * np.log2(n)
def O_n_squared(n): return n**2
def O_2_n(n): return 2**n

# 2. Input sizes
n_large = np.arange(1, 1001)
n_small = np.arange(1, 21)  # for exponential only

# 3. Plotting
plt.figure(figsize=(12, 8))
plt.plot(n_large, O_1(n_large), label='O(1)', linewidth=2)
plt.plot(n_large, O_log_n(n_large), label='O(log n)', linewidth=2)
plt.plot(n_large, O_n(n_large), label='O(n)', linewidth=2)
plt.plot(n_large, O_n_log_n(n_large), label='O(n log n)', linewidth=2)
plt.plot(n_large, O_n_squared(n_large), label='O(n^2)', linewidth=2)
plt.plot(n_small, O_2_n(n_small), label='O(2^n)', linewidth=2, linestyle='dashed')

plt.title("Big-O Time Complexity Growth")
plt.xlabel("Input Size (n)")
plt.ylabel("Operations Count")
plt.legend()
plt.grid
