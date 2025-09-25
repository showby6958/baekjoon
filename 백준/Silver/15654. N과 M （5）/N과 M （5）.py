n, m = map(int, input().split())

nums = list(map(int, input().split()))

nums.sort()
res = []

def dfs():
    if len(res) == m:
        print(' '.join(map(str, res)))
        return

    for i in range(n):
        if nums[i] in res:
            continue

        res.append(nums[i])
        dfs()
        res.pop()

dfs()