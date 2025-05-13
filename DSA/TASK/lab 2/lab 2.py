# task 1

class DynamicArray:
    def __init__(self):
        self.capacity = 2  # initial capacity
        self.length = 0
        self.array = self._make_array(self.capacity)

    def _make_array(self, size):
        return [None] * size

    def _resize(self, new_capacity):
        new_array = self._make_array(new_capacity)
        for i in range(self.length):
            new_array[i] = self.array[i]
        self.array = new_array
        self.capacity = new_capacity

    def append(self, item):
        if self.length == self.capacity:
            self._resize(2 * self.capacity)
        self.array[self.length] = item
        self.length += 1

    def insert(self, index, item):
        if index < 0 or index > self.length:
            raise IndexError("Index out of bounds")
        if self.length == self.capacity:
            self._resize(2 * self.capacity)
        for i in range(self.length, index, -1):
            self.array[i] = self.array[i - 1]
        self.array[index] = item
        self.length += 1

    def delete(self, index):
        if index < 0 or index >= self.length:
            raise IndexError("Index out of bounds")
        for i in range(index, self.length - 1):
            self.array[i] = self.array[i + 1]
        self.array[self.length - 1] = None
        self.length -= 1
        if 0 < self.length < self.capacity // 4:
            self._resize(self.capacity // 2)

    def search(self, item):
        for i in range(self.length):
            if self.array[i] == item:
                return i
        return -1

    def __str__(self):
        return "[" + ", ".join(str(self.array[i]) for i in range(self.length)) + "]"

# task 2

def longest_substring_brute_force(s):
    max_len = 0
    longest = ""
    for i in range(len(s)):
        seen = set()
        current = ""
        for j in range(i, len(s)):
            if s[j] in seen:
                break
            seen.add(s[j])
            current += s[j]
        if len(current) > max_len:
            max_len = len(current)
            longest = current
    return longest, max_len

#2. Sliding Window Method (O(n))
def longest_substring_sliding_window(s):
    start = 0
    seen = {}
    max_len = 0
    longest = ""

    for end in range(len(s)):
        if s[end] in seen and seen[s[end]] >= start:
            start = seen[s[end]] + 1
        seen[s[end]] = end
        if end - start + 1 > max_len:
            max_len = end - start + 1
            longest = s[start:end+1]

    return longest, max_len

#3. Execution Time Comparison
import time

def test_performance(s):
    print(f"Testing string: {s}")

    start = time.time()
    result1 = longest_substring_brute_force(s)
    end = time.time()
    print(f"Brute Force Result: {result1}, Time: {end - start:.6f} sec")

    start = time.time()
    result2 = longest_substring_sliding_window(s)
    end = time.time()
    print(f"Sliding Window Result: {result2}, Time: {end - start:.6f} sec")

#4. Test Cases
test_performance("abcabcbb")
test_performance("bbbbb")
test_performance("pwwkew")
test_performance("dvdf")
test_performance("a" * 1000 + "b")  # long input


# task 3
# Python Code (In-Place Rotation without Extra Space)
def rotate_matrix(matrix):
    n = len(matrix)
    
    # Step 1: Transpose the matrix
    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # Step 2: Reverse each row
    for row in matrix:
        row.reverse()

    return matrix
 # Test Case 

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print("Original matrix:")
for row in matrix:
    print(row)

rotate_matrix(matrix)

print("\nRotated matrix (90° clockwise):")
for row in matrix:
    print(row)
 

