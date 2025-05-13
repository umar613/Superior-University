# task 1

# Memoization (Top-Down Approach)
def fib_memoization(n, memo={}):
    if n <= 1:
        return n
    if n not in memo:
        memo[n] = fib_memoization(n - 1, memo) + fib_memoization(n - 2, memo)
    return memo[n]

# Tabulation (Bottom-Up Approach)
def fib_tabulation(n):
    if n <= 1:
        return n
    dp = [0] * (n + 1)
    dp[1] = 1
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    return dp[n]

# Example usage:
print(fib_memoization(10))  # Output: 55
print(fib_tabulation(10))  # Output: 55


# task 2

# Recursive + Memoization
def lcs_memoization(X, Y, m, n, memo={}):
    if m == 0 or n == 0:
        return 0
    if (m, n) not in memo:
        if X[m - 1] == Y[n - 1]:
            memo[(m, n)] = 1 + lcs_memoization(X, Y, m - 1, n - 1, memo)
        else:
            memo[(m, n)] = max(lcs_memoization(X, Y, m - 1, n, memo), lcs_memoization(X, Y, m, n - 1, memo))
    return memo[(m, n)]

# Tabulation (Bottom-Up Approach)
def lcs_tabulation(X, Y):
    m = len(X)
    n = len(Y)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if X[i - 1] == Y[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    
    return dp[m][n]

# Example usage:
print(lcs_memoization("AGGTAB", "GXTXAYB", len("AGGTAB"), len("GXTXAYB")))  # Output: 4 (GTAB)
print(lcs_tabulation("AGGTAB", "GXTXAYB"))  # Output: 4 (GTAB)


# task 3

def knapsack(weights, values, capacity):
    n = len(weights)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        for w in range(1, capacity + 1):
            if weights[i - 1] <= w:
                dp[i][w] = max(dp[i - 1][w], values[i - 1] + dp[i - 1][w - weights[i - 1]])
            else:
                dp[i][w] = dp[i - 1][w]
    
    return dp[n][capacity]

# Example usage:
weights = [2, 3, 4, 5]
values = [3, 4, 5, 6]
capacity = 5
print(knapsack(weights, values, capacity))  # Output: 7
