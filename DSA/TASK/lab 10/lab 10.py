# task 1

import time
import random

# Linear Search Implementation
def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i  # Return the index of the target
    return -1  # Return -1 if the target is not found

# Binary Search Implementation
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid 
        elif arr[mid] < target:
            left = mid + 1  
        else:
            right = mid - 1  
    return -1  # Return -1 if the target is not found

# Function to measure the execution time of search algorithms
def measure_time(search_func, arr, target):
    start_time = time.time()
    search_func(arr, target)
    return time.time() - start_time

# Function to test the search algorithms on different list sizes
def test_search_algorithms():
    sizes = [1000, 5000, 10000]
    linear_times = []
    binary_times = []

    for size in sizes:
        # Create a random list for Linear Search (unsorted)
        arr_linear = random.sample(range(1, size * 10), size)
        # Create a sorted list for Binary Search
        arr_binary = sorted(arr_linear)

        # Pick a random target element from the array
        target = random.choice(arr_linear)

        # Measure execution times
        linear_times.append(measure_time(linear_search, arr_linear, target))
        binary_times.append(measure_time(binary_search, arr_binary, target))

    # Printing times for comparison
    for i in range(len(sizes)):
        print(f"Size: {sizes[i]} - Linear Search: {linear_times[i]:.6f} sec, Binary Search: {binary_times[i]:.6f} sec")

# Run the comparison test
test_search_algorithms()

# Example Test Cases
arr = [10, 23, 45, 70, 11, 15]
print(f"Linear Search result for 45: {linear_search(arr, 45)}")  # Output: 2 (index of 45)

sorted_arr = [10, 15, 23, 45, 70]
print(f"Binary Search result for 45: {binary_search(sorted_arr, 45)}")  # Output: 3 (index of 45)


# task 2

import math
import time
import random

# Jump Search Implementation
def jump_search(arr, target):
    n = len(arr)
    step = int(math.sqrt(n))  # Optimal block size (step)

    prev = 0
    while arr[min(step, n) - 1] < target:
        prev = step
        step += int(math.sqrt(n))
        if prev >= n:
            return -1  # Target not in the list
    
    # Linear search within the block
    for i in range(prev, min(step, n)):
        if arr[i] == target:
            return i
    return -1  # Target not found

# Interpolation Search Implementation
def interpolation_search(arr, target):
    low, high = 0, len(arr) - 1

    while low <= high and target >= arr[low] and target <= arr[high]:
        # Estimate the position using the interpolation formula
        pos = low + ((target - arr[low]) * (high - low)) // (arr[high] - arr[low])

        # If the target is found
        if arr[pos] == target:
            return pos
        elif arr[pos] < target:
            low = pos + 1
        else:
            high = pos - 1
    return -1  # Target not found

# Binary Search Implementation (for comparison)
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1  # Target not found

# Function to measure execution time for search algorithms
def measure_time(search_func, arr, target):
    start_time = time.time()
    search_func(arr, target)
    return time.time() - start_time

# Function to test and compare the performance of the search algorithms
def test_search_algorithms():
    sizes = [1000, 5000, 10000]
    jump_times = []
    interpolation_times = []
    binary_times = []

    for size in sizes:
        # Create a random sorted list for the search algorithms
        arr = sorted(random.sample(range(1, size * 10), size))

        # Pick a random target element from the array
        target = random.choice(arr)

        # Measure execution times
        jump_times.append(measure_time(jump_search, arr, target))
        interpolation_times.append(measure_time(interpolation_search, arr, target))
        binary_times.append(measure_time(binary_search, arr, target))

    # Printing times for comparison
    for i in range(len(sizes)):
        print(f"Size: {sizes[i]} - Jump Search: {jump_times[i]:.6f} sec, Interpolation Search: {interpolation_times[i]:.6f} sec, Binary Search: {binary_times[i]:.6f} sec")

# Run the comparison test
test_search_algorithms()

# Example Test Cases
arr = [1, 3, 5, 7, 9, 11, 13, 15]
print(f"Jump Search result for 7: {jump_search(arr, 7)}")  # Output: 3 (index of 7)
print(f"Interpolation Search result for 7: {interpolation_search(arr, 7)}")  # Output: 3 (index of 7)
print(f"Binary Search result for 7: {binary_search(arr, 7)}")  # Output: 3 (index of 7)


# task 3

import math
import time
import random

# Exponential Search Implementation
def exponential_search(arr, target):
    # If the element is at the first index
    if arr[0] == target:
        return 0
    
    # Find the range for binary search by increasing the index exponentially
    n = len(arr)
    i = 1
    while i < n and arr[i] <= target:
        i *= 2

    # Perform Binary Search between the range [i//2, min(i, n-1)]
    return binary_search(arr, target, i // 2, min(i, n - 1))

def binary_search(arr, target, low, high):
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

# Fibonacci Search Implementation
def fibonacci_search(arr, target):
    n = len(arr)
    fib_m_minus_2 = 0
    fib_m_minus_1 = 1
    fib_m = fib_m_minus_1 + fib_m_minus_2
    
    # Find the largest Fibonacci number less than or equal to n
    while fib_m < n:
        fib_m_minus_2 = fib_m_minus_1
        fib_m_minus_1 = fib_m
        fib_m = fib_m_minus_1 + fib_m_minus_2

    # Perform Fibonacci Search
    offset = -1
    while fib_m > 1:
        i = min(offset + fib_m_minus_2, n - 1)

        if arr[i] == target:
            return i
        elif arr[i] < target:
            fib_m = fib_m_minus_1
            fib_m_minus_1 = fib_m_minus_2
            fib_m_minus_2 = fib_m - fib_m_minus_1
            offset = i
        else:
            fib_m = fib_m_minus_2
            fib_m_minus_1 = fib_m_minus_1 - fib_m_minus_2
            fib_m_minus_2 = fib_m - fib_m_minus_1

    if fib_m_minus_1 and arr[offset + 1] == target:
        return offset + 1

    return -1

def measure_time(search_func, arr, target):
    start_time = time.time()
    search_func(arr, target)
    return time.time() - start_time

def test_search_algorithms():
    sizes = [1000, 5000, 10000]
    exp_times = []
    fib_times = []
    jump_times = []
    binary_times = []

    for size in sizes:
        
        arr = sorted(random.sample(range(1, size * 10), size))

        
        target = random.choice(arr)

        exp_times.append(measure_time(exponential_search, arr, target))
        fib_times.append(measure_time(fibonacci_search, arr, target))
        jump_times.append(measure_time(jump_search, arr, target))
        binary_times.append(measure_time(binary_search, arr, target))

    # Printing times for comparison
    for i in range(len(sizes)):
        print(f"Size: {sizes[i]} - Exponential Search: {exp_times[i]:.6f} sec, Fibonacci Search: {fib_times[i]:.6f} sec, Jump Search: {jump_times[i]:.6f} sec, Binary Search: {binary_times[i]:.6f} sec")

# Run the comparison test
test_search_algorithms()

# Example Test Cases
arr = [2, 4, 8, 16, 32, 64, 128]
print(f"Exponential Search result for 32: {exponential_search(arr, 32)}")  # Output: 4 (index of 32)
print(f"Fibonacci Search result for 32: {fibonacci_search(arr, 32)}")  # Output: 4 (index of 32)
