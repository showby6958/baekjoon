from collections import deque

f, s, g, u, d = list(map(int, input().split()))


def bfs():
    visited = [False] * (f + 1)
    q = deque()
    q.append((s, 0)) # (현재 층, 버튼 누른 횟수)
    visited[s] = True

    while q:
        floor, count = q.popleft()

        # 목표층 도착
        if floor == g:
            return count

        # 위로 이동
        nu = floor + u
        if nu <= f and not visited[nu]:
            visited[nu] = True
            q.append((nu, count + 1))
        
        # 아래로 이동
        nd = floor - d
        if nd >= 1 and not visited[nd]:
            visited[nd] = True
            q.append((nd, count + 1))

    return "use the stairs" # 도달 불가

print(bfs())