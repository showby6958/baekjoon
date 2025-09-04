from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
graph = []

for _ in range(n):
    graph.append(list(map(int, input().split())))

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

def bfs(graph, a, b):
    q = deque()
    q.append((a, b))
    graph[a][b] = 0
    count = 1

    while q:
        x, y = q.popleft()
        for a in range(4):
            nx = x+dx[a]
            ny = y+dy[a]
            # 범위 안에 있고
            if 0 <= nx < n and 0 <= ny < m:
                # 해당 위치가 방문 안했으면(=1), 탐색 시작
                if graph[nx][ny] == 1:
                    # 방문 했으니까 현재 위치 0으로 바꾸기
                    graph[nx][ny] = 0
                    q.append((nx, ny))
                    # 해당 위치를 탐색했으니까 count +1(그림의 한 픽셀을 탐색완료한 것)
                    count += 1
    return count

paint = []
for i in range(n):
    for j in range(m):
        # 현재 위치가 방문 안했으면(1), 시작
        if graph[i][j] == 1:
            paint.append(bfs(graph, i, j))

# 그림 출력
# 그림이 없는경우 둘 다 0
if len(paint) == 0:
    print(len(paint)) # 0
    print(0) # 0
else:
    print(len(paint)) # 그림 개수
    print(max(paint)) # 가장 큰 그림 크기