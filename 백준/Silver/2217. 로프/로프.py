n = int(input())

roap = []
result = []

for i in range(n):
    roap.append(int(input()))

roap.sort(reverse=True)

for i in range(n):
    result.append(roap[i]*(i+1))

print(max(result))