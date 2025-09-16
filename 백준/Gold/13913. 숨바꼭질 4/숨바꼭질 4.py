from collections import deque

n, k = map(int, input().split())
q = deque()

limit = 100001
cnt = [0] * limit
visited = [0]*limit
graph = [-1] * limit
 
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def bfs(x, target):
    q.append(x)
    visited[x] = 1
    while q:
        x = q.popleft()
        
        if x == target:
            return cnt[x]

        for i in (x*2, x+1, x-1):
            if 0 <= i < limit and not visited[i]:
                q.append(i)
                visited[i] = 1
                cnt[i] = cnt[x] + 1
                graph[i] = x

print(bfs(n, k))

path = []
temp = k
while temp != -1:
    path.append(temp)
    temp = graph[temp]

path.reverse()
print(" ".join(map(str, path)))