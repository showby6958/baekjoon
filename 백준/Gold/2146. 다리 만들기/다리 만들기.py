from collections import deque

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]


dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

# 섬 레이블링
def label_bfs(graph, n):
    visited = [[False] * n for _ in range(n)]
    island_id = 1

    for i in range(n):
        for j in range(n):
            # 아직 방문하지 않은 땅(1) 발견 = 새로운 섬 발견
            if graph[i][j] == 1 and not visited[i][j]:
                q = deque()
                q.append((i, j))
                visited[i][j] = True
                # 섬 ID 부여 (원래 1 -> island_id)
                graph[i][j] = island_id
    
                while q:
                    x, y = q.popleft()
                    for i in range(4):
                        nx = x + dx[i]
                        ny = y + dy[i]
                        # 인덱스 범위 내, 
                        if 0 <= nx < n and 0 <= ny < n:
                            # 같은 섬인 경우, 방문하지 않은 경우
                            if graph[nx][ny] == 1 and not visited[nx][ny]:
                                visited[nx][ny] = True
                                # 해당 섬을 island_id로 채우기(1번 섬이면 1로 가득, 2번 섬이면 2로 가득)
                                graph[nx][ny] = island_id
                                q.append((nx, ny))
                # 첫 번째 섬 = 1, 두 번째 섬 = 2 ... 섬 레이블링
                island_id += 1

    # 그래프와 섬 개수 리턴
    return graph, island_id-1 

# 최단거리 구하기
def bfs(island_id, n):
    q = deque()
    dist = [[-1] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if graph[i][j] == island_id:
                q.append((i, j))
                dist[i][j] = 0

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 인덱스 범위 내
            if 0 <= nx < n and 0 <= ny < n:
                # 다른 섬을 만난 경우
                if graph[nx][ny] != island_id and graph[nx][ny] != 0:
                    return dist[x][y]
                
                # 아직 방문 안된 바다인 경우 해당 섬 소속으로 확장
                if graph[nx][ny] == 0 and dist[nx][ny] == -1:
                    dist[nx][ny] = dist[x][y] + 1
                    q.append((nx, ny))


graph, island_id = label_bfs(graph, n)
answer = 10**9
for id in range(1, island_id+1):
    answer = min(answer, bfs(id, n))

print(answer)