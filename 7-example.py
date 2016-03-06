w = 5
h = 4

def dfs():
    def _dfs(nw, nh):
        if nw > w or nh > h:
            return 0
        if nw == w and nh == h:
            return 1
        return _dfs(nw+1, nh) + _dfs(nw, nh+1)
    return _dfs(0, 0)

def dfs_memo():
    dp = [[0]*(w+1) for _ in range(h+1)]
    def _dfs(nw, nh):
        if nw > w or nh > h:
            return 0
        if nw == w and nh == h:
            return 1
        if dp[nh][nw] == 0:
            dp[nh][nw] = _dfs(nw+1, nh) + _dfs(nw, nh+1)
        return dp[nh][nw]
    return _dfs(0, 0)

def dp():
    dp = [[0]*(w+1) for _ in range(h+1)]
    dp[0][0] = 1
    for nh in range(h+1):
        for nw in range(w+1):
            if nh != 0:
                dp[nh][nw] += dp[nh-1][nw]
            if nw != 0:
                dp[nh][nw] += dp[nh][nw-1]
    return dp[h][w]

print dfs()
print dfs_memo()
print dp()


