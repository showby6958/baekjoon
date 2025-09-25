import sys
input = sys.stdin.readline

n = int(input())

lines = [list(map(int, input().split())) for _ in range(n)]

lines.sort()


left = lines[0][0]
right = lines[0][1]
length = 0 

for i in range(1, n):
    if right >= lines[i][1]:
        continue
    elif lines[i][0] <= right < lines[i][1]:
        right = lines[i][1]
    
    # 선이 떨어져 있는 경우는 따로 길이 계산
    elif right < lines[i][0]:
        length += (right - left)
        left, right = lines[i][0], lines[i][1]
      

# 연결된 선의 길이 계산
length += right - left
print(length)