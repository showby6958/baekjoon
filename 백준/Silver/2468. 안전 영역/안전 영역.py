from collections import deque

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def bfs(x, y, h, visited):
    q = deque()
    q.append((x, y))
    visited[x][y] = True

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if not visited[nx][ny] and graph[nx][ny] > h:
                    visited[nx][ny] = True
                    q.append((nx, ny))
                

max_height = max(map(max, graph))
result = 0

for h in range(max_height + 1):
    visited = [[False] * n for _ in range(n)]
    count = 0
    for i in range(n):
        for j in range(n):
            # 방문하지 않았고, 해당 좌표의 높이가 h 보다 높은 경우
            if not visited[i][j] and graph[i][j] > h:
                bfs(i, j, h, visited)
                count += 1
    result = max(result, count)

print(result)