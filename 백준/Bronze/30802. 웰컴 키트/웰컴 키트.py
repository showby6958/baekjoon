N = int(input())
size = map(int, input().split())
T, P = map(int, input().split())
res = 0

for i in size:
    if i == 0:
        continue
    elif i <= T:
        res += 1
    elif i % T == 0:
        res += i // T
    else:
        res += (i // T) + 1
    
print(res)
print(N//P, N%P)