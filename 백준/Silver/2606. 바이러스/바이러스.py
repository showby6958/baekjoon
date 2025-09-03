import sys
input = sys.stdin.readline

n = int(input())
m = int(input())

graph = [[] for _ in range(n+1)]

for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

    
visited = [0] * (n+1)
def dfs(node):
    visited[node] = 1
    for next_node in graph[node]:
        if not visited[next_node]:
            dfs(next_node)


dfs(1)

# 1번 컴퓨터 제외 (-1)
print(sum(visited)-1)