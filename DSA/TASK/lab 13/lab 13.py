# task 1

def activity_selection(activities):
    # Sort activities based on their finish time
    activities.sort(key=lambda x: x[1])
    
    selected_activities = []
    last_finish_time = -1
    
    # Select activities that do not overlap
    for activity in activities:
        start, end = activity
        if start >= last_finish_time:
            selected_activities.append(activity)
            last_finish_time = end
    
    return selected_activities

# Example usage:
activities = [(1, 3), (2, 5), (3, 9), (6, 8), (8, 11)]
print(activity_selection(activities))  # Expected Output: [(1, 3), (6, 8), (8, 11)]


#  task 2

import heapq
from collections import defaultdict

# Helper function to build the Huffman Tree
class Node:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None
    
    def __lt__(self, other):
        return self.freq < other.freq

def build_huffman_tree(freq_map):
    heap = [Node(char, freq) for char, freq in freq_map.items()]
    heapq.heapify(heap)
    
    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)
        merged = Node(None, left.freq + right.freq)
        merged.left = left
        merged.right = right
        heapq.heappush(heap, merged)
    
    return heap[0]

# Helper function to generate Huffman codes
def generate_codes(node, current_code, codes):
    if node is None:
        return
    if node.char is not None:
        codes[node.char] = current_code
    generate_codes(node.left, current_code + "0", codes)
    generate_codes(node.right, current_code + "1", codes)

# Main function to encode the string
def huffman_encoding(text):
    # Count the frequency of each character in the text
    freq_map = defaultdict(int)
    for char in text:
        freq_map[char] += 1
    
    # Build the Huffman Tree
    root = build_huffman_tree(freq_map)
    
    # Generate Huffman codes
    codes = {}
    generate_codes(root, "", codes)
    
    return codes

# Example usage:
text = "hello greedy"
huffman_codes = huffman_encoding(text)
print(huffman_codes)


# task 3

class DisjointSet:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n
    
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])  # Path compression
        return self.parent[x]
    
    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        
        if rootX != rootY:
            if self.rank[rootX] > self.rank[rootY]:
                self.parent[rootY] = rootX
            elif self.rank[rootX] < self.rank[rootY]:
                self.parent[rootX] = rootY
            else:
                self.parent[rootY] = rootX
                self.rank[rootX] += 1
            return True
        return False

def kruskal(edges, num_vertices):
    # Sort edges based on weight
    edges.sort(key=lambda x: x[2])
    
    mst = []
    disjoint_set = DisjointSet(num_vertices)
    
    # Process edges in increasing order of weight
    for u, v, weight in edges:
        if disjoint_set.union(u, v):
            mst.append((u, v, weight))
    
    return mst

# Example usage:
edges = [(0, 1, 4), (0, 2, 3), (1, 2, 1), (1, 3, 2), (2, 3, 4)]
num_vertices = 4
print(kruskal(edges, num_vertices))  # Expected Output: [(1, 2, 1), (1, 3, 2), (0, 2, 3)]
