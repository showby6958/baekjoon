import sys
from collections import deque

input = sys.stdin.readline

T = int(input())

count = 0

for _ in range(T):
    n, m = map(int, input().split())
    weight = list(map(int, input().split()))

    queue = deque(range(n))
    count = 0

    while queue:
        current = queue.popleft()

        if any(weight[current] < weight[i] for i in queue):
            queue.append(current)
        else:
            count += 1
            if current == m:
                print(count)
                break