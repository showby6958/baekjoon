import sys

N = int(input())
li = []

for _ in range(N):
    li.append(int(sys.stdin.readline()))

for i in sorted(li):
    print(i)