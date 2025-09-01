import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    combinations = {}
    n = int(input().strip())
    for _ in range(n):
        wear, category = input().split()
        if category in combinations:
            combinations[category].append(wear)
        else:
            combinations[category] = [wear]

    cnt = 1

    for i in combinations:
        cnt *= (len(combinations[i]) + 1)
    
    print(cnt-1)