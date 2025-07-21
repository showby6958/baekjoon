L = int(input())
alphabet = input()
M = 1234567891
res = 0



def alphabet_to_number(alphabet):
    return ord(alphabet) - ord('a') + 1


for i in range(L):
    res = (res + alphabet_to_number(alphabet[i]) * (31**i)) % M

print(res)

