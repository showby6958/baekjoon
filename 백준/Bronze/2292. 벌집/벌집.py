n = int(input())

num_room = 1
cnt = 1

while n > num_room :
    num_room += 6 * cnt
    cnt += 1
        
print(cnt)
