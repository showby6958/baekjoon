from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
graph = []

for _ in range(n):
    graph.append(list(map(int, input().rstrip())))

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

def bfs(graph, a, b):
    q = deque()
    q.append((a, b))

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if graph[nx][ny] == 1:
                    # 현재 위치를 탐색하고 +1을 하고 그것을 큐에 저장해놓음(이전 탐색 위치의 값을 알 수 있음)
                    # 그다음 탐색할 위치는 이전에 탐색한 위치의 값 +1을 하면서 계속 진행
                    # 원래 1(길)이었던 칸들을 BFS로 탐색하면서 지금 까지 온 거리로 덮어 씀
                    graph[nx][ny] = graph[x][y] + 1
                    q.append((nx, ny))
    # n,m 위치의 값을 리턴
    return graph[n-1][m-1]

print(bfs(graph, 0, 0))