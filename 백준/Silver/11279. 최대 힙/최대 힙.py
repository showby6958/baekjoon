import sys
import heapq

input = sys.stdin.readline

n = int(input())
max_heap = []

# 파이썬의 heap은 min_heap 이다.
# max_heap인 경우 heappush, heappop 할 때 모두 -를 붙이면 됨(그럼 min_heap이랑 똑같음)
for _ in range(n):
    x = int(input())
    if x > 0:
        heapq.heappush(max_heap, -x)
    else:
        if not max_heap:
            print(0)
        else:
            print(-heapq.heappop(max_heap))