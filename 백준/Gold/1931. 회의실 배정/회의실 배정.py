import sys
input = sys.stdin.readline

n = int(input())
count = 0
arr = []
for _ in range(n):
    i, j = map(int, input().split())
    arr.append([i, j])

arr.sort(key=lambda x: (x[1], x[0]))

tmp = 0
for start, end in arr:
    if tmp <= start:
        count += 1
        tmp = end

print(count)