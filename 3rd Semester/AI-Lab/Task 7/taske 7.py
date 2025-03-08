# taske 1 A* Algorithm Code
import heapq

class Node:
    def __init__(self, position, parent=None):
        self.position=position
        self.parent=parent
        self.g=0
        self.h=0
        self.f=0

    def __eq__(self, other):
        return self.position==other.position

def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def a_star(start, goal, grid):
    open_list=[]
    closed_list=[]

    start_node=Node(start)
    goal_node=Node(goal)
    heapq.heappush(open_list, (start_node.f, start_node))

    while open_list:
        current_node=heapq.heappop(open_list)[1]
        closed_list.append(current_node)

        if current_node==goal_node:
            path=[]
            while current_node:
                path.append(current_node.position)
                current_node=current_node.parent
            return path[::-1]
        
        neighbors = [
            (current_node.position[0] + 1, current_node.position[1]),
            (current_node.position[0] - 1, current_node.position[1]),
            (current_node.position[0], current_node.position[1] + 1),
            (current_node.position[0], current_node.position[1] - 1)
        ]

        for next_position in neighbors:

            if (0 <=next_position[0] < len(grid)) and (0 <=next_position[1] < len(grid[0])) and grid[next_position[0]][next_position[1]] == 0:
                neighbor_node=Node(next_position, current_node)

                if neighbor_node in closed_list:
                    continue
                neighbor_node.g=current_node.g + 1
                neighbor_node.h=heuristic(neighbor_node.position, goal_node.position)
                neighbor_node.f=neighbor_node.g + neighbor_node.h

                if any(neighbor_node==node[1] and neighbor_node.g >=node[1].g for node in open_list):
                    continue
                heapq.heappush(open_list, (neighbor_node.f, neighbor_node))

    return None

grid = [
[0, 0, 0, 0, 0],
[0, 1, 1, 1, 0],
[0, 0, 0, 0, 0],
[0, 1, 1, 1, 0],
[0, 0, 0, 0, 0]
]

start=(0, 0)
goal=(4, 4)

path=a_star(start, goal, grid)
if path:
    print("Path found:", path)
else:
    print("No path found.")