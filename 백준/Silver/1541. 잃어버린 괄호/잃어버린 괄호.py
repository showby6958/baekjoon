arr = input().split('-')
result = 0

arr2 = arr[0].split('+')


for i in arr2:
    result += int(i)

for j in arr[1:]:
    for k in j.split('+'):
        result -= int(k)

print(result)