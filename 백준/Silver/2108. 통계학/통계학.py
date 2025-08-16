from collections import Counter
import sys

input = sys.stdin.readline
n = int(input())

lst = [int(input()) for _ in range(n)]


# 산술평균
mean = sum(lst) / n
print(round(mean))

# 중앙값
sorted_lst = sorted(lst)
n = len(lst)
median = sorted_lst[n//2]
print(median)

# 중앙값 - 짝수도 포함할 경우
# median = int((sorted_lst[n//2] + sorted_lst[n//2-1]) / 2 if n%2==0 else sorted_lst[n//2])
# print(median)

# 최빈값
counter = Counter(lst)
freq_lst = counter.most_common()

modes = []

max_count = freq_lst[0][1]

# 최빈값 리스트 modes 만들기
for num, cnt in freq_lst:
    if cnt == max_count:
        modes.append(num)

# 최빈값 여러 개면 두 번째로 작은 값 출력
if len(modes) > 1:
    modes.sort()
    print(modes[1])
else:
    print(modes[0])


# 범위
ran = max(lst) - min(lst)
print(ran)