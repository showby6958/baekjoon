from collections import deque

n, k = map(int, input().split())
q = deque()

limit = 100001
cnt = [0] * limit
visited = [0]*limit

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def bfs(x, target):
    q.append(x)

    while q:
        x = q.popleft()
        
        # 수빈이 동생을 찾은 경우 cnt 출력
        if x == target:
            return cnt[x]
            break

        # 이동한 위치의 cnt를 1씩 증가 시키면서 이동한 거리를 표기
        # x*2로 순간이동 하는 경우
        if 0 <= x*2 < limit and not visited[x*2]:
            q.append(x*2)
            cnt[x*2] = cnt[x] # 순간이동은 0초만에 움직여서 cnt 증가 X
            visited[x*2] = 1
        
        # x-1로 걷는 경우 
        if 0 <= x-1 < limit and not visited[x-1]:
            q.append(x-1)
            cnt[x-1] = cnt[x] + 1
            visited[x-1] = 1
        
        # x+1로 걷는 경우
        if 0 <= x+1 < limit and not visited[x+1]:
            q.append(x+1)
            cnt[x+1] = cnt[x] + 1
            visited[x+1] = 1

        

print(bfs(n, k))