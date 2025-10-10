def dfs(k, s, res, depth):
    if len(res) == 6:
        print(*res)
        return

    for i in range(depth, k):
        if not s[i] in res:
            res.append(s[i])
            depth += 1
            dfs(k, s, res, depth)
            res.pop()


while True:
    s = list(map(int, input().split()))
    k = s[0]
    s = s[1:]
    if k == 0:
        break
    
    res = []
    dfs(k, s, res, 0)
    print()
