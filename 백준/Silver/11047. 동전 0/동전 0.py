# 그리디 알고리즘
import sys
input = sys.stdin.readline

n, k = map(int, input().split())

coins = []
for _ in range(n):
    coins.append(int(input()))

    coins.sort(reverse=True)
    result = 0

for i in coins:
    result += k // i
    k = k % i


print(result)