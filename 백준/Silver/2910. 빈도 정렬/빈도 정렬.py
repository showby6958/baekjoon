import sys
input = sys.stdin.readline

n, c = map(int, input().split())

nums = list(map(int, input().split()))

freq = {} # 빈도
order = [] # 등장 순서

for x in nums:
    if x in freq:
        freq[x] += 1
    else:
        freq[x] = 1
        order.append(x)

order.sort(key=lambda x: freq[x], reverse=True)


res = []
for i in order:
    res.extend([str(i)] * freq[i])

print(" ".join(res))