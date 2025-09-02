import sys
from collections import deque
input = sys.stdin.readline

n, k = map(int, input().split())
max = 100000
dist = [0] * (max + 1)

def bfs():
    q = deque()
    q.append(n)
    while q:
        x = q.popleft()
        # 수빈 위치(x) 와 
        if x == k:
            print(dist[x])
            break
        for i in (x-1, x+1, x*2):
            if 0 <= i <= max and dist[i] == 0:
                dist[i] = dist[x] + 1
                q.append(i)
            
bfs()