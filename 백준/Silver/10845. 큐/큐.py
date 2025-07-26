import sys
from collections import deque

N = int(input())

queue = deque()

while N > 0:
    cmd = sys.stdin.readline().strip().split()
    if len(cmd) == 0:
        continue
        
    if cmd[0] == 'push':
        queue.append(cmd[1])
    elif cmd[0] == 'pop':
        if len(queue) == 0:
            print(-1)
        else:
            print(queue.popleft())
    elif cmd[0] == 'size':
        print(len(queue))
    elif cmd[0] == 'empty':
        if len(queue) == 0:
            print(1)
        else:
            print(0)
    elif cmd[0] == 'front':
        if len(queue) != 0:
            print(queue[0])
        else: 
            print(-1)
            
    elif cmd[0] == 'back':
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[-1])
    N -= 1