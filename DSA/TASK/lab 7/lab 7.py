# taske 1

class Heap:
    def __init__(self, heap_type="min"):
        self.heap = []
        self.type = heap_type  # "min" or "max"

    def _compare(self, a, b):
        return a < b if self.type == "min" else a > b

    def insert(self, value):
        self.heap.append(value)
        self._heapify_up(len(self.heap) - 1)

    def extract_root(self):
        if not self.heap:
            return None
        root = self.heap[0]
        last = self.heap.pop()
        if self.heap:
            self.heap[0] = last
            self._heapify_down(0)
        return root

    def peek(self):
        return self.heap[0] if self.heap else None

    def heapify(self, array):
        self.heap = array[:]
        for i in reversed(range(len(self.heap) // 2)):
            self._heapify_down(i)

    def _heapify_up(self, index):
        parent = (index - 1) // 2
        while index > 0 and self._compare(self.heap[index], self.heap[parent]):
            self.heap[index], self.heap[parent] = self.heap[parent], self.heap[index]
            index, parent = parent, (parent - 1) // 2

    def _heapify_down(self, index):
        size = len(self.heap)
        while True:
            left, right = 2 * index + 1, 2 * index + 2
            target = index
            if left < size and self._compare(self.heap[left], self.heap[target]):
                target = left
            if right < size and self._compare(self.heap[right], self.heap[target]):
                target = right
            if target == index:
                break
            self.heap[index], self.heap[target] = self.heap[target], self.heap[index]
            index = target

# teast cases
# Min-Heap
min_heap = Heap("min")
min_heap.insert(10)
min_heap.insert(5)
min_heap.insert(20)
min_heap.insert(2)
print("Min-Heap root:", min_heap.extract_root())  # Output: 2

# Max-Heap
max_heap = Heap("max")
max_heap.insert(10)
max_heap.insert(5)
max_heap.insert(20)
max_heap.insert(2)
print("Max-Heap root:", max_heap.extract_root())  # Output: 20

# Heapify Example
arr = [9, 4, 7, 1, -2, 6, 5]
h = Heap("min")
h.heapify(arr)
print("Min-Heap from array:", h.heap)



# task 2

import heapq

class PriorityQueue:
    def __init__(self):
        self.heap = []
        self.count = 0

    def enqueue(self, value, priority):
        heapq.heappush(self.heap, (priority, self.count, value))
        self.count += 1

    def dequeue(self):
        if not self.heap:
            return None
        return heapq.heappop(self.heap)[2]

    def peek(self):
        if not self.heap:
            return None
        return self.heap[0][2]

pq = PriorityQueue()
pq.enqueue("Task A", 3)
pq.enqueue("Task B", 1)
pq.enqueue("Task C", 2)

print(pq.dequeue())
print(pq.peek())
print(pq.dequeue())
  
# task 3

import heapq

def find_k_smallest(arr, k):
    """Returns the K smallest elements from the array using a Min-Heap."""
    return heapq.nsmallest(k, arr)

def find_k_largest(arr, k):
    """Returns the K largest elements from the array using a Max-Heap."""
    return heapq.nlargest(k, arr)

# Test cases
arr = [10, 4, 3, 20, 15, 7]
print("K smallest elements:", find_k_smallest(arr, 3)) 
print("K largest elements:", find_k_largest(arr, 2))    


