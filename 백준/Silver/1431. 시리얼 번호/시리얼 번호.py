import sys
input = sys.stdin.readline

n = int(input())

def sum_nums(inputs):
    result = 0
    for i in inputs:
        if i.isdigit():
            result += int(i)
    return result


arr = []
for i in range(n):
    a = input().strip()
    arr.append(a)
    
arr.sort(key=lambda x: (len(x), sum_nums(x), x))
for i in arr:
    print(i)