from itertools import combinations


N, M = map(int, input().split())
nums = list(map(int, input().split()))
res = 0
max_sum = -1

for comb in combinations(nums, 3):
    total = sum(comb)
    if total <= M:
        max_sum = max(max_sum, total)

print(max_sum)