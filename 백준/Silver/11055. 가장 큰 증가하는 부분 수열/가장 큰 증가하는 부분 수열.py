import sys

input = sys.stdin.readline

n = int(input())
array = list(map(int, input().split()))

d = [0] * n

d[0] = array[0]

for i in range(1, n):
    # 현재 인덱스까지 모든 수 확인 i번째 라면, i번째 이전까지 나올 수 있는 최대 값("증가하는 부분수열", "현재 인덱스" 중 최댓값)
    for j in range(i):
        if array[i] > array[j]:
            # 현재 인덱스의 값이 큰 경우 j를 더했을 때와 비교하여 max값 갱신
            d[i] = max(d[i], array[i] + d[j])
        else: 
            d[i] = max(d[i], array[i])
           



print(max(d))