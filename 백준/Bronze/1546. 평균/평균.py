n = int(input())
arr = list(map(int, input().split()))

res = []

m = max(arr)
for i in arr:
    res.append(i / m*100)
    
print(sum(res) / n)
