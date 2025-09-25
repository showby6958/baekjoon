n, m = map(int, input().split())

res = []

def dfs(start):
    if len(res) == m:
        print(' '.join(map(str, res)))
        return
    
    for i in range(start, n+1):
        res.append(i)
        dfs(1)
        res.pop()

dfs(1)