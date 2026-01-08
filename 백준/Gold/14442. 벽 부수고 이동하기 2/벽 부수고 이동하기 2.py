from collections import deque
import sys

input = sys.stdin.readline

n, m, k = map(int, input().split())
graph = [list(map(int, input().strip())) for _ in range(n)]

visited = [[[0]* (k+1) for _ in range(m)] for _ in range(n)]

dx = [0, 0 ,-1, 1]
dy = [-1, 1, 0, 0]

def bfs():
    q = deque()
    q.append((0, 0, k))

    visited[0][0][k] = 1 # 시작 거리 1

    while q:
        x, y, remain = q.popleft()
        d = visited[x][y][remain]

        # 도착
        if (x, y) == (n-1, m-1):
            return visited[x][y][remain]

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx < n and 0 <= ny < m:
                # 벽 아닌 경우
                if graph[nx][ny] == 0 and visited[nx][ny][remain] == 0:
                    visited[nx][ny][remain] = d + 1
                    q.append((nx, ny, remain))
                # 벽 부술 경우
                elif graph[nx][ny] == 1 and remain > 0 and visited[nx][ny][remain-1] == 0: 
                    visited[nx][ny][remain-1] = d + 1
                    q.append((nx, ny, remain-1))

    return -1


print(bfs())