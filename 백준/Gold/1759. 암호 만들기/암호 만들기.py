l, c = map(int, input().split())

alphabet = list(input().split())
alphabet.sort()

vowels = ['a', 'e', 'i', 'o', 'u']
res = []

def check(password):
    v_cnt = 0
    c_cnt = 0
    
    for i in password:
        if i in vowels:
            v_cnt += 1
        else:
            c_cnt += 1

    if v_cnt >= 1 and c_cnt >= 2:
        return True
    else:
        return False   


def dfs(start):
    if len(res) == l:
        if check(res):
            print(''.join(res))
        return
        
    for i in range(start, c):
        res.append(alphabet[i])
        dfs(i+1)
        res.pop()

dfs(0)
