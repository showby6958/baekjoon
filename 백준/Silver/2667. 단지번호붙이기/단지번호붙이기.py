from collections import deque

n = int(input())


graph = []

for _ in range(n):
    graph.append(list(map(int, input())))
    

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def bfs(x, y):
    q = deque()
    q.append((x, y))
    graph[x][y] = 0
    area = 1

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and graph[nx][ny] == 1:
                q.append([nx, ny])
                graph[nx][ny] = 0
                area += 1

    return area

areas = []
for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            areas.append(bfs(i, j))
areas.sort()
print(len(areas))
for i in areas:
    print(i)