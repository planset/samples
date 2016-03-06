import sys

products = [
    ['A', 3, 2],
    ['B', 4, 3],
    ['C', 1, 2],
    ['D', 2, 3],
    ['E', 3, 6]
    ]
products = [
    ['A', 3000000000, 2],
    ['B', 4000000000, 3],
    ['C', 1000000000, 2],
    ['D', 2000000000, 3],
    ['E', 3000000000, 6]
    ]

MAX_WEIGHT = 10
MAX_WEIGHT = 10000000000

def dfs():
    def _dfs(n, w):
        if w > MAX_WEIGHT:
            return -sys.maxint-1
        if n >= len(products):
            return 0
        return max(_dfs(n+1, w),
                   _dfs(n+1, w+products[n][1]) + products[n][2])
    return _dfs(0, 0)

def dfs_memo():
    dp = [[-1]*(MAX_WEIGHT+1) for _ in range(6)]
    def _dfs(n, w):
        if w > MAX_WEIGHT:
            return -sys.maxint-1
        if n >= len(products):
            return 0
        if dp[n][w] < 0:
            dp[n][w] = max(_dfs(n+1, w), 
                    _dfs(n+1, w+products[n][1]) + products[n][2])
        return dp[n][w]
    return _dfs(0, 0)

def dfs_dp():
    dp = [[0]*(MAX_WEIGHT+1) for _ in range(6)]
    dp[0][0] = 0
    ret = 0
    p = products
    for n in range(5):
        for w in range(MAX_WEIGHT+1):
            nw = w + p[n][1]
            if nw <= MAX_WEIGHT: 
                dp[n+1][nw] = max(dp[n+1][nw], dp[n][w] + p[n][2])
                ret = max(dp[n+1][nw], ret)
    return ret


print dfs()
print dfs_memo()
print dfs_dp()


