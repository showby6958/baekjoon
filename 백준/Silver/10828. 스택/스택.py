import sys
n = int(input())
stack = []
input = sys.stdin.readline


for  _ in range(n):
    cmd = input().strip().split() # 공백 기준으로 나누기
    if cmd[0] == "push":
        stack.append(int(cmd[1])) # push 뒤에 오는 정수를 스택에 저장
        # print(stack[-1])
    elif cmd[0] == "pop":
        if stack:
            print(stack.pop())
        else:
            print(-1)
    elif cmd[0] == "size":
        print(len(stack))
    elif cmd[0] == "empty":
        if stack:
            print(0)
        else:
            print(1)
    elif cmd[0] == "top":
        if stack:
            print(stack[-1])
        else:
            print(-1)
