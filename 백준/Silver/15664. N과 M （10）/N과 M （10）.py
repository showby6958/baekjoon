n, m = map(int, input().split())

nums = list(map(int, input().split()))
nums.sort()

res = []
visited = [False] * n

def dfs(start):
    if len(res) == m:
        print(' '.join(map(str, res)))
        return
    
    temp = 0
    # 중복 없애기 위해서 dfs(i+1)로 그 다음 인덱스를 추가
    # 1 7 9 9 인 경우, 결과 9 9 <- 서로 다른 9임
    for i in range(start, len(nums)):
        if not visited[i] and temp != nums[i]:
            res.append(nums[i])
            visited[i] = True
            temp = nums[i]
            dfs(i+1)
            res.pop()
            visited[i] = False

dfs(0)