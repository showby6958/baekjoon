n = int(input())
arr = []
cnt = 0

result = []
for _ in range(n):
    arr.append(int(input()))


# result.append(arr[-1])
for i in range(n-1, 0, -1):
    if arr[i-1] >= arr[i]:
        cnt += arr[i-1] - arr[i] + 1
        arr[i-1] = arr[i] - 1
        # print(arr[i-1])
        # result.append(arr[i-1])
    # else:
    #     result.append(arr[i-1])

# 결과 arr 출력
# print(result)

# 횟수 출력
print(cnt)