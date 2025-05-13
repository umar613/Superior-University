# task 1

class HashTable:
    def __init__(self, size, use_chaining=True):
        self.size = size
        self.use_chaining = use_chaining
        if self.use_chaining:
            # Chaining with linked list (using lists in this case)
            self.table = [None] * size
        else:
            # Open Addressing (Linear Probing)
            self.table = [None] * size

    def hash_function(self, key):
        return hash(key) % self.size

    def insert(self, key, value):
        index = self.hash_function(key)
        
        if self.use_chaining:
            # Chaining: Using linked lists (just lists here)
            if self.table[index] is None:
                self.table[index] = [(key, value)]
            else:
                # Check for existing key and update
                for i, (k, v) in enumerate(self.table[index]):
                    if k == key:
                        self.table[index][i] = (key, value)
                        return
                # If key doesn't exist, append
                self.table[index].append((key, value))
        else:
            # Open Addressing: Linear Probing
            start_index = index
            while self.table[index] is not None:
                if self.table[index][0] == key:
                    # Update existing key-value pair
                    self.table[index] = (key, value)
                    return
                index = (index + 1) % self.size
                if index == start_index:  # If we looped back to the start
                    break
            self.table[index] = (key, value)

    def get(self, key):
        index = self.hash_function(key)
        
        if self.use_chaining:
            if self.table[index] is not None:
                for k, v in self.table[index]:
                    if k == key:
                        return v
        else:
            start_index = index
            while self.table[index] is not None:
                if self.table[index][0] == key:
                    return self.table[index][1]
                index = (index + 1) % self.size
                if index == start_index:
                    break
        return None

    def delete(self, key):
        index = self.hash_function(key)
        
        if self.use_chaining:
            if self.table[index] is not None:
                for i, (k, v) in enumerate(self.table[index]):
                    if k == key:
                        del self.table[index][i]
                        return True
        else:
            start_index = index
            while self.table[index] is not None:
                if self.table[index][0] == key:
                    self.table[index] = None
                    return True
                index = (index + 1) % self.size
                if index == start_index:
                    break
        return False


# Example Usage:
ht = HashTable(10, use_chaining=True)
ht.insert("name", "Alice")
ht.insert("age", 25)
print(ht.get("name"))  # Output: Alice
ht.delete("age")
print(ht.get("age"))   # Output: None


# task 2

import matplotlib.pyplot as plt

def custom_hash(key):
    return sum(ord(c) for c in key) % 10

def test_hash_function(hash_func):
    keys = ["hello", "world", "python", "hashing", "test", "collision", "data", "structure"]
    hash_values = [hash_func(key) for key in keys]
    return hash_values

# Test custom hash function
hash_values_custom = test_hash_function(custom_hash)

# Compare with Python's built-in hash function
hash_values_builtin = test_hash_function(hash)

# Plot histograms
plt.hist(hash_values_custom, bins=range(11), alpha=0.5, label='Custom Hash Function')
plt.hist(hash_values_builtin, bins=range(11), alpha=0.5, label='Built-in hash()')
plt.legend(loc='upper right')
plt.xlabel('Hash Values')
plt.ylabel('Frequency')
plt.title('Comparison of Custom Hash Function and Built-in hash()')
plt.show()


# task 3

class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = {}
        self.head = Node(0, 0)  # Dummy head
        self.tail = Node(0, 0)  # Dummy tail
        self.head.next = self.tail
        self.tail.prev = self.head

    def _remove(self, node):
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node

    def _add(self, node):
        head_next = self.head.next
        self.head.next = node
        node.prev = self.head
        node.next = head_next
        head_next.prev = node

    def get(self, key):
        if key in self.cache:
            node = self.cache[key]
            self._remove(node)
            self._add(node)
            return node.value
        return -1

    def put(self, key, value):
        if key in self.cache:
            node = self.cache[key]
            self._remove(node)
            node.value = value
            self._add(node)
        else:
            node = Node(key, value)
            self.cache[key] = node
            self._add(node)
            if len(self.cache) > self.capacity:
                tail_node = self.tail.prev
                self._remove(tail_node)
                del self.cache[tail_node.key]


# Test LRU Cache
cache = LRUCache(2)
cache.put(1, "A")
cache.put(2, "B")
print(cache.get(1))  # Output: "A"
cache.put(3, "C")    # Removes least recently used key (2)
print(cache.get(2))  # Output: -1 (not found)

