import sys
input = sys.stdin.readline


# 에라토스테네스의 체
M, N = map(int, input().strip().split())
is_prime = [True] * (N + 1)
is_prime[0] = is_prime[1] = False

# 2 부터 루트N 까지 반복해서 배수 제거(N 보다 작은 약수 중 하나는 루트N 이하에 반드시 존재)
for i in range(2, int(N ** 0.5) + 1):
    if is_prime[i]:
        # i*i 부터 시작 -> i 보다 작은 배수는 이미 이전 소수 단계에서 제거됨
        for j in range(i*i, N+1, i):
            is_prime[j] = False


# M 이상 N 이하 범위에서 소수 출력
for num in range(M, N+1):
    if is_prime[num]:
        print(num)