n, m = map(int, input().split())

nums = list(map(int, input().split()))
nums.sort()

res = []

def dfs(start):
    if len(res) == m:
        print(' '.join(map(str, res)))
        return

    for i in range(start, len(nums)):
        if not nums[i] in res:
            res.append(nums[i])
            dfs(i+1)
            res.pop()

dfs(0)