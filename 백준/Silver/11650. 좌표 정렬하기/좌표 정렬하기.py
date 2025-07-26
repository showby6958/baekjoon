N = int(input())
array = []


for i in range(N):
    [a, b] = map(int, input().split())
    array.append([a, b])


s_array = sorted(array, key = lambda x: (x[0], x[1]))


for j in range(N):
    print(s_array[j][0], s_array[j][1])