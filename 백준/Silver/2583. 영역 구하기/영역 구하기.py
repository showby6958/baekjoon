import sys
from collections import deque
input = sys.stdin.readline

m, n, k = map(int, input().split()) # m: 세로, n: 가로

graph = [[0]*(n) for _ in range(m)] # (y, x)

# 직사각형 부분을 1로 채우기
# 문제에서 (x1, y1)은 왼쪽 아래, (x2, y2)는 오른쪽 위 좌표
# graph[y][x] 방식으로 접근
# BFS로 graph[y][x] == 0 인 곳을 탐색해서 하나의 영역 넓이 구하기
# 영역 개수와 넓이들을 오름차순 정렬해서 출력
for _ in range(k):
    x1, y1, x2, y2 = map(int, input().split())
    for y in range(y1, y2):
        for x in range(x1, x2):
            graph[y][x] = 1

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def bfs(x, y):
    q = deque()
    q.append((x, y))
    graph[y][x] = 1
    area = 1
    
    while q:
        x, y = q.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and graph[ny][nx] == 0:
                graph[ny][nx] = 1
                q.append((nx, ny))
                area += 1
    return area


areas = []
for y in range(m):
    for x in range(n):
        if graph[y][x] == 0:
            areas.append(bfs(x, y))

areas.sort()
print(len(areas))
print(*areas)