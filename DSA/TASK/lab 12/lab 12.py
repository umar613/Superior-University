 # task 1

class Graph:
    def __init__(self, directed=True):
        self.directed = directed
        self.adj_list = {}
        self.adj_matrix = []
        self.vertices = []

    def add_vertex(self, vertex):
        # Add a vertex to the graph
        if vertex not in self.adj_list:
            self.adj_list[vertex] = []
            self.vertices.append(vertex)

            # Update the adjacency matrix for the new vertex
            for row in self.adj_matrix:
                row.append(0)  # Append 0 for the new vertex in each row
            self.adj_matrix.append([0] * len(self.vertices))  # Add new row for the new vertex

    def add_edge(self, vertex1, vertex2, weight=1):
        # Add an edge from vertex1 to vertex2 with a given weight
        if vertex1 not in self.adj_list or vertex2 not in self.adj_list:
            return  # Ensure both vertices exist
        
        self.adj_list[vertex1].append(vertex2)

        # For adjacency matrix representation
        index1 = self.vertices.index(vertex1)
        index2 = self.vertices.index(vertex2)
        self.adj_matrix[index1][index2] = weight
        
        # For undirected graphs, add the reverse edge
        if not self.directed:
            self.adj_list[vertex2].append(vertex1)
            self.adj_matrix[index2][index1] = weight

    def display_adj_list(self):
        # Display adjacency list representation
        print("Adjacency List:", self.adj_list)

    def display_adj_matrix(self):
        # Display adjacency matrix representation
        print("Adjacency Matrix:")
        print("   ", " ".join(self.vertices))
        for i, vertex in enumerate(self.vertices):
            print(vertex, self.adj_matrix[i])

# Example usage:
g = Graph(directed=False)
g.add_vertex("A")
g.add_vertex("B")
g.add_vertex("C")
g.add_edge("A", "B", 4)
g.add_edge("A", "C", 1)
g.add_edge("B", "C", 2)
g.display_adj_list()
g.display_adj_matrix()


# task 2

from collections import deque

class Graph:
    def __init__(self, directed=True):
        self.directed = directed
        self.adj_list = {}

    def add_vertex(self, vertex):
        if vertex not in self.adj_list:
            self.adj_list[vertex] = []

    def add_edge(self, vertex1, vertex2):
        if vertex1 not in self.adj_list:
            self.add_vertex(vertex1)
        if vertex2 not in self.adj_list:
            self.add_vertex(vertex2)
        self.adj_list[vertex1].append(vertex2)
        if not self.directed:
            self.adj_list[vertex2].append(vertex1)

    def bfs(self, start):
        visited = set()
        queue = deque([start])
        traversal_order = []

        while queue:
            vertex = queue.popleft()
            if vertex not in visited:
                visited.add(vertex)
                traversal_order.append(vertex)
                for neighbor in self.adj_list[vertex]:
                    if neighbor not in visited:
                        queue.append(neighbor)
        return traversal_order

    def dfs(self, start):
        visited = set()
        traversal_order = []

        def dfs_recursive(vertex):
            visited.add(vertex)
            traversal_order.append(vertex)
            for neighbor in self.adj_list[vertex]:
                if neighbor not in visited:
                    dfs_recursive(neighbor)

        dfs_recursive(start)
        return traversal_order

# Example usage:
g = Graph()
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 3)
g.add_edge(2, 3)
print(g.bfs(0))  # Output: [0, 1, 2, 3]
print(g.dfs(0))  # Output: [0, 1, 3, 2] (DFS order can vary)


# task 3

import heapq

class Graph:
    def __init__(self):
        self.adj_list = {}

    def add_vertex(self, vertex):
        if vertex not in self.adj_list:
            self.adj_list[vertex] = []

    def add_edge(self, vertex1, vertex2, weight):
        if vertex1 not in self.adj_list:
            self.add_vertex(vertex1)
        if vertex2 not in self.adj_list:
            self.add_vertex(vertex2)
        self.adj_list[vertex1].append((vertex2, weight))
        self.adj_list[vertex2].append((vertex1, weight))  # For undirected graph

    def dijkstra(self, start):
        # Dijkstra's algorithm using a priority queue (min-heap)
        distances = {vertex: float('inf') for vertex in self.adj_list}
        distances[start] = 0
        priority_queue = [(0, start)]
        while priority_queue:
            current_distance, current_vertex = heapq.heappop(priority_queue)

            if current_distance > distances[current_vertex]:
                continue

            for neighbor, weight in self.adj_list[current_vertex]:
                distance = current_distance + weight
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    heapq.heappush(priority_queue, (distance, neighbor))

        return distances

# Example usage:
g = Graph()
g.add_edge("A", "B", 4)
g.add_edge("A", "C", 1)
g.add_edge("B", "C", 2)
g.add_edge("B", "D", 5)
g.add_edge("C", "D", 1)
print(g.dijkstra("A"))  # Output: {'A': 0, 'B': 3, 'C': 1, 'D': 2}
