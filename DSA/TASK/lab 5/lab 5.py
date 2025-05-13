# taske 1
class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class HashTableChaining:
    def __init__(self, size=100):
        self.size = size
        self.table = [None] * self.size

    def _hash(self, key):
        return hash(key) % self.size

    def insert(self, key, value):
        index = self._hash(key)
        new_node = Node(key, value)
        if not self.table[index]:
            self.table[index] = new_node
        else:
            current = self.table[index]
            while current.next:
                current = current.next
            current.next = new_node

    def get(self, key):
        index = self._hash(key)
        current = self.table[index]
        while current:
            if current.key == key:
                return current.value
            current = current.next
        return None

    def delete(self, key):
        index = self._hash(key)
        current = self.table[index]
        prev = None
        while current:
            if current.key == key:
                if prev:
                    prev.next = current.next
                else:
                    self.table[index] = current.next
                return True
            prev = current
            current = current.next
        return False

    def display(self):
        for i in range(self.size):
            current = self.table[i]
            if current:
                print(f"Index {i}: ", end="")
                while current:
                    print(f"({current.key}, {current.value})", end=" -> ")
                    current = current.next
                print()
            else:
                print(f"Index {i}: None")


class HashTableLinearProbing:
    def __init__(self, size=100):
        self.size = size
        self.table = [None] * self.size

    def _hash(self, key):
        return hash(key) % self.size

    def insert(self, key, value):
        index = self._hash(key)
        original_index = index
        while self.table[index] is not None:
            if self.table[index][0] == key:  # Update the value if key exists
                self.table[index] = (key, value)
                return
            index = (index + 1) % self.size
            if index == original_index:
                raise Exception("Hash table is full")
        self.table[index] = (key, value)

    def get(self, key):
        index = self._hash(key)
        original_index = index
        while self.table[index] is not None:
            if self.table[index][0] == key:
                return self.table[index][1]
            index = (index + 1) % self.size
            if index == original_index:
                return None
        return None

    def delete(self, key):
        index = self._hash(key)
        original_index = index
        while self.table[index] is not None:
            if self.table[index][0] == key:
                self.table[index] = None
                return True
            index = (index + 1) % self.size
            if index == original_index:
                return False
        return False

    def display(self):
        for i in range(self.size):
            if self.table[i] is not None:
                print(f"Index {i}: {self.table[i]}")
            else:
                print(f"Index {i}: None")


# Test Cases
if __name__ == "__main__":
    print("Testing Chaining Hash Table:")
    htc = HashTableChaining(10)
    htc.insert("apple", 1)
    htc.insert("banana", 2)
    htc.insert("cherry", 3)
    print("Value for 'banana':", htc.get("banana"))
    htc.display()
    htc.delete("banana")
    print("After deleting 'banana':")
    htc.display()

    print("\nTesting Linear Probing Hash Table:")
    htlp = HashTableLinearProbing(10)
    htlp.insert("apple", 1)
    htlp.insert("banana", 2)
    htlp.insert("cherry", 3)
    print("Value for 'banana':", htlp.get("banana"))
    htlp.display()
    htlp.delete("banana")
    print("After deleting 'banana':")
    htlp.display()

# taske 2

def are_anagrams(str1, str2):
    if len(str1) != len(str2):
        return False

    freq = {}

    for char in str1:
        freq[char] = freq.get(char, 0) + 1

    for char in str2:
        if char not in freq:
            return False
        freq[char] -= 1
        if freq[char] < 0:
            return False

    return True

# Test cases
print(are_anagrams("listen", "silent"))     # True
print(are_anagrams("hello", "world"))       # False
print(are_anagrams("triangle", "integral")) # True
print(are_anagrams("abc", "abcd"))          # False
print(are_anagrams("aabbcc", "abcabc"))     # True
 

# taske 3
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
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def _remove(self, node):
        p = node.prev
        n = node.next
        p.next = n
        n.prev = p

    def _add(self, node):
        p = self.tail.prev
        p.next = node
        node.prev = p
        node.next = self.tail
        self.tail.prev = node

    def get(self, key):
        if key in self.cache:
            node = self.cache[key]
            self._remove(node)
            self._add(node)
            return node.value
        return -1

    def put(self, key, value):
        if key in self.cache:
            self._remove(self.cache[key])
        node = Node(key, value)
        self.cache[key] = node
        self._add(node)
        if len(self.cache) > self.capacity:
            lru = self.head.next
            self._remove(lru)
            del self.cache[lru.key]

    def display(self):
        current = self.head.next
        result = []
        while current != self.tail:
            result.append((current.key, current.value))
            current = current.next
        print("Cache state:", result)

cache = LRUCache(5)
cache.put(1, "A")
cache.put(2, "B")
cache.put(3, "C")
cache.put(4, "D")
cache.put(5, "E")
cache.get(2)
cache.put(6, "F")
cache.get(4)
cache.put(7, "G")
cache.get(6)
cache.put(8, "H")
cache.put(9, "I")
cache.put(10, "J")
cache.display()
