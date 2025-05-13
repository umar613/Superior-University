# task 1
import time
import random
import matplotlib.pyplot as plt

# Bubble Sort function
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

# Selection Sort function
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr

# Insertion Sort function
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

# Function to measure the execution time of sorting algorithms
def measure_time(sort_func, arr):
    start_time = time.time()
    sort_func(arr)
    return time.time() - start_time

# Function to test the sorting algorithms on different list sizes
def test_algorithms():
    sizes = [100, 200, 300, 400, 500, 1000]
    bubble_times = []
    selection_times = []
    insertion_times = []

    for size in sizes:
        arr = random.sample(range(1, size * 10), size)  # Create a random list
        bubble_times.append(measure_time(bubble_sort, arr.copy()))
        selection_times.append(measure_time(selection_sort, arr.copy()))
        insertion_times.append(measure_time(insertion_sort, arr.copy()))

    # Plotting the performance comparison
    plt.figure(figsize=(10, 6))
    plt.plot(sizes, bubble_times, label="Bubble Sort", marker='o')
    plt.plot(sizes, selection_times, label="Selection Sort", marker='o')
    plt.plot(sizes, insertion_times, label="Insertion Sort", marker='o')
    plt.xlabel("List Size")
    plt.ylabel("Execution Time (seconds)")
    plt.title("Sorting Algorithm Performance Comparison")
    plt.legend()
    plt.show()

# Run the comparison test
test_algorithms()

# task 2

import time
import random

# Quick Sort implementation
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

# Merge Sort implementation
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)

# Helper function to merge two sorted arrays (used in Merge Sort)
def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

# Function to measure the execution time of sorting algorithms
def measure_time(sort_func, arr):
    start_time = time.time()
    sort_func(arr)
    return time.time() - start_time

# Function to test the sorting algorithms on different list sizes
def test_algorithms():
    sizes = [1000, 5000, 10000]
    quick_times = []
    merge_times = []

    for size in sizes:
        arr = random.sample(range(1, size * 10), size)  # Create a random list
        quick_times.append(measure_time(quick_sort, arr.copy()))
        merge_times.append(measure_time(merge_sort, arr.copy()))

    # Printing times for comparison
    for i in range(len(sizes)):
        print(f"Size: {sizes[i]} - Quick Sort: {quick_times[i]:.6f} sec, Merge Sort: {merge_times[i]:.6f} sec")

# Run the comparison test
test_algorithms()


# task 3
def heapify(arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[left] > arr[largest]:
        largest = left
    if right < n and arr[right] > arr[largest]:
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

def heap_sort(arr):
    n = len(arr)

    # Build max heap
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # Extract elements one by one from the heap
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # Swap
        heapify(arr, i, 0)

    return arr


