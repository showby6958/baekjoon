from  collections import deque
n, m = map(int, input().split())
q = deque()
graph = [list(map(int, input())) for _ in range(n)]

# 1층 = 벽을 뚫지 않은 경우, 2층 = 벽을 뚫은 경우
visited = [[[0]*2 for _ in range(m)] for _ in range(n)]

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def bfs(x, y):
    q.append((x, y, 0))
    visited[x][y][0] = 1
    while q:
        # z = 벽은 부쉈는지 체크 (1=벽을 부숨)
        x, y, z = q.popleft()
        
        # 도착했다면 벽 부순 횟수 포함한 visited값 리턴
        if (x, y) == (n-1, m-1):
            return visited[x][y][z]

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny][z]:
                # 벽이 아닌 경우
                if not graph[nx][ny]:
                    visited[nx][ny][z] = visited[x][y][z] + 1
                    q.append((nx, ny, z))
                
                # 벽이 있는데 벽을 부순적이 없는 경우(벽 부수기 가능)
                if graph[nx][ny] and not z:
                    visited[nx][ny][1] = visited[x][y][z] + 1
                    q.append((nx, ny, 1))
                    # z = 1로 벽을 부쉈다는것을 큐에 저장(이후에 벽을 못 부숨)
    # 불가능한 경우
    return -1


print(bfs(0, 0))