from collections import deque

n, m, v_start = map(int, input().split())

# 그래프 생성
graph = [[] for _ in range(n+1)]
for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

# 그래프 오름차순 정렬
for i in range(1, n+1):
    graph[i].sort()

dfs_visited = [False] * (n+1)

def dfs(node):
    print(node, end=" ")
    dfs_visited[node] = True
    for a in graph[node]:
        if not dfs_visited[a]:
            dfs(a)


def bfs(start):
    visited = [False] * (n+1)
    q = deque()
    q.append(start)
    visited[start] = True

    while q:
        node = q.popleft()
        print(node, end=" ")
        for a in graph[node]:
            if not visited[a]:
                q.append(a)
                visited[a] = True

dfs(v_start)
print()
bfs(v_start)