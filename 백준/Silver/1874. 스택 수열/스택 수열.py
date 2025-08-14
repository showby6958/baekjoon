n = int(input())
sequence = [int(input()) for _ in range(n)]

stack = [] 
result = [] # +, - 기록
current = 1 # push할 다음 숫자
possible = True

for num in sequence:
    # num 까지 push
    while current <= num:
        stack.append(current)
        result.append('+')
        current += 1
    
    # 스택의 top이 num이면 pop
    if stack and stack[-1] == num:
        stack.pop()
        result.append('-')
    else:
        # 만들 수 없는 경우
        possible = False
        break

# 출력
if possible:
    print('\n'.join(result))
else:
    print("NO")

