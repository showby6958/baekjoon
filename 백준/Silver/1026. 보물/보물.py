n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))


s=0
for i in range(n):
    s += min(a) * max(b)
    a.remove(min(a))
    b.remove(max(b))

print(s)