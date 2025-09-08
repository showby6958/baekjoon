import sys 
from collections import deque
input = sys.stdin.readline

t = int(input())

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

def bfs(graph, x, y):
    q = deque()
    q.append([x, y])
    graph[x][y] = 0 # 방문처리: 표기된 1을 0으로 바꾸기
    
    while q: # q가 비었다 = 탐색 가능한 연속 영역을 모두 탐색했다.
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]        
            ny = y + dy[i]
            if 0 <= nx < m and 0 <= ny < n and graph[nx][ny] == 1:
                q.append([nx, ny])
                graph[nx][ny] = 0
                
                    


for _ in range(t):
    m, n, k = map(int, input().split())
    graph = [[0]*(n) for _ in range(m)] # 빈 배추밭

    for _ in range(k):
        a, b = map(int, input().split())
        graph[a][b] = 1 # 배추 위치 표시

    count = 0
    for j in range(m):
        for k in range(n):
            if graph[j][k] == 1:
                bfs(graph, j, k)
                count += 1 # bfs 함수 호출될 때마다 = 하나의 연속 영역이 끝날 때마다
    print(count)