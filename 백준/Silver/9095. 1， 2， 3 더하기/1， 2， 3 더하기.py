import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    
    if n < 0:
        break
    
    dp = [0] * (n+1)
    dp[0] = 1 # 합이 0 (아무것도 더하지 않는 경우)
    
    for i in range(1, n+1):
        if i-1 >= 0:
            dp[i] += dp[i-1]
        if i-2 >= 0:
            dp[i] += dp[i-2]
        if i-3 >= 0:
            dp[i] += dp[i-3]

    print(dp[n])


# dp = [1, 1, 2, 4, 7, ...]

# dp[1] = 1 # 1 (방법 1가지)
# dp[2] = 2 # 1+1, 2 (방법 2가지)
# dp[3] = 4 # 1+1+1, 1+2, 2+1, 3

# 즉, dp[i] = dp[i-1] + dp[i-2] + d[i-3] 로 나타내짐
# dp[1] = dp[0] = 1가지 
# dp[2] = dp[1] + dp[0] = 1 + 1 = 2가지 
# dp[3] = dp[2] + dp[1] + dp[0] = 2 + 1 + 1 = 4
# dp[4] = dp[3] + dp[2] + dp[1] = 4 + 2 + 1 = 7가지