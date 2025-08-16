import sys

input = sys.stdin.readline

m = int(input())

s = []
    
for _ in range(m):
    i = list(input().split())
    if i[0] == "add":
        if i[1] in s:
            continue
        else:
            s.append(i[1])

    elif i[0] == "remove":
        if i[1] in s:
            s.remove(i[1])
        else:
            continue
    
    elif i[0] == "check":
        if i[1] in s:
            print(1)
        else:
            print(0)

    elif i[0] == "toggle":
        if i[1] in s:
            s.remove(i[1])
        else:
            s.append(i[1])

    elif i[0] == "all":
        s.clear()
        s.extend(map(str, range(1, 21)))

    elif i[0] == "empty":
        s.clear()

