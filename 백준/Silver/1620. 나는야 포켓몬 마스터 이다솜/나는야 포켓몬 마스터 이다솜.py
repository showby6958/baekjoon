import sys
input = sys.stdin.readline

n, m = map(int, input().split())
pokemon = []

dic_index = {}
dic_name = {}

# 양방향 딕셔너리 만들기 
for i in range(1, n+1):
    name = input().strip()
    dic_name[str(i)] = name
    dic_index[name] = str(i)    

for _ in range(m):
    target = input().strip()
    if target in dic_name:
        print(dic_name[target])
    else:
        print(dic_index[target])
