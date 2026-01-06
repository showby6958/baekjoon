import sys 
input = sys.stdin.readline
from collections import Counter

n = int(input())
nums = [int(input()) for _ in range(n)]

c = Counter(nums)


ans = min(c.items(), key=lambda x: (-x[1], x[0]))
print(ans[0])

