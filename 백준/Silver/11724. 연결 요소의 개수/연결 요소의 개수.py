import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())

graph = [[] for _ in range(n+1)]


for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)


def bfs(start):
    q = deque()
    q.append(start)
    visited[start] = True
    
    while q:
        node = q.popleft()
        for a in graph[node]:
            if not visited[a]:
                q.append(a)
                visited[a] = True


visited = [False] * (n+1)
count = 0



for i in range(1, n+1):
    if not visited[i]:
        bfs(i)
        count += 1

print(count)



