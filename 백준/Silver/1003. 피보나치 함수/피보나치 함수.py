import sys
input = sys.stdin.readline

t = int(input())

dp = [0, 1]

for i in range(2, 41):
    dp.append(dp[i-1] + dp[i-2])

for _ in range(t):
    n = int(input())
    if n == 0:
        print(1, 0)
    else:
        print(dp[n-1], dp[n])