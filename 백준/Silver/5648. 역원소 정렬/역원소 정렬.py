import sys
input = sys.stdin.read

n, *data = input().split()

arr = []
for i in data:
    arr.append(int(i[::-1]))
    
arr.sort()

for r in arr:
    print(r)