import sys
input = sys.stdin.readline
n = int(input())
stack = []

lst = [int(input()) for _ in range(n)]

for num in lst:
    if num == 0:
        stack.pop()
    else:
        stack.append(num)
    
print(sum(stack))