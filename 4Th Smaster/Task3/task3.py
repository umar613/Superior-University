def water_jug_dfs(jugA_capacity, jugB_capacity, target):
    visited = set()
    path = []
    def dfs(state):
        a, b = state

        if state in visited:
            return False
        visited.add(state)

        if a == target:
            path.append((state, "Goal reached"))
            return True
    
        possible_moves = [
            ((jugA_capacity, b), "Fill Jug A"),
            ((a, jugB_capacity), "Fill Jug B"),
            ((0, b), "Empty Jug A"),
            ((a, 0), "Empty Jug B"),
            ((max(0, a - (jugB_capacity - b)), min(jugB_capacity, b + a)), "pour A B"),
            ((min(jugA_capacity, a + b), max(0, b - (jugA_capacity - a))), "pour B A"),
        ]

        for new_state, action in possible_moves:
            if new_state not in visited:
                path.append((state, action))
                if dfs(new_state):
                    return True
                path.pop()

        return False

    initial_state = (0, 0)
    if dfs(initial_state):
        print("Solution found!\nSteps:")
        for state, action in path:
            print(f"{action}  {state}")
    else:
        print("No solution found.")

water_jug_dfs(4, 3, 2)