N = int(input())
nature_num = list(map(int, input().split()))
res = 0

for num in nature_num:
    if num < 2:
        continue
    is_prime = True

    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            is_prime = False
            break

    if is_prime:
        res += 1

        
print(res)
        