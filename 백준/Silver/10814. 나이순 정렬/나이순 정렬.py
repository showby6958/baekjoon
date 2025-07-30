N = int(input())
user_lst = []

for _ in range(N):
    age, name = input().split()
    user_lst.append((int(age), name))


sorted_lst = sorted(user_lst, key=lambda x: x[0])


for age, name in sorted_lst:
    print(age, name)