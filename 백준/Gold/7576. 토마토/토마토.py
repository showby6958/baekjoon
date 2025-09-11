from collections import deque

m, n = map(int, input().split())


graph = [list(map(int, input().split())) for _ in range(n)]

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

q =deque()

# 1. 익은 토마토(1) 모두 큐에 넣기
for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            q.append((i, j))


while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                # 안 익은 토마토(0), BFS로 퍼질 때 익게됨(graph[x][y] + 1)
                # BFS가 끝나면 graph[i][j]에 각 토마토가 익은 날짜가 저장됨
                if graph[nx][ny] == 0:
                    graph[nx][ny] = graph[x][y] + 1
                    q.append((nx, ny))


result = 0
for i in range(n):
    for j in range(m):
        if graph[i][j] == 0:
            print(-1)
            exit(0)
        result = max(result, graph[i][j])

print(result - 1)