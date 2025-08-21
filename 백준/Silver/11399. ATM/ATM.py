import sys
input = sys.stdin.readline

n = int(input())
p = []
total = 0
temp = 0

p = list(map(int, input().split()))

p.sort()

for i in p:
    temp += i
    total += temp

print(total)