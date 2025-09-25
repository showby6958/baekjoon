import heapq
import sys
input = sys.stdin.readline
n = int(input())

lecture = [list(map(int, input().split())) for _ in range(n)]

lecture.sort()

heap = []

for s, e in lecture:
    if heap and heap[0] <= s: # 기존 강의실 사용가능
        heapq.heappop(heap)
    heapq.heappush(heap, e) # 강의 끝나는 시간 push

print(len(heap))