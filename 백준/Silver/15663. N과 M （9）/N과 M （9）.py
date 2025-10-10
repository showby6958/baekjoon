n, m = map(int, input().split())

nums = list(map(int, input().split()))
nums.sort()

res = []
visited = [False] * n

def dfs():
    if len(res) == m:
        print(' '.join(map(str, res)))
        return

    temp = 0
    # visited를 이용해서 한 번 탐색한 인덱스를 배제
    # visited를 사용하지 않은 경우 단순 문자 비교이기 때문에,
    # 1 7 9 9 인 경우 세번째 9와 네번째 9를 구분 못함
    for i in range(n):
        if not visited[i] and temp != nums[i]:
            res.append(nums[i])
            visited[i] = True
            temp = nums[i]
            dfs()
            visited[i] = False
            res.pop()
            

dfs()