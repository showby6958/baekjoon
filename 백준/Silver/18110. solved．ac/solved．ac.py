import sys

N = int(sys.stdin.readline())


def rounding_f(num):
    if num - int(num) >= 0.5:
        return int(num) + 1
    else :
        return int(num)



if N == 0:
    print(0)
    
else:
    opinions = sorted([int(sys.stdin.readline()) for _ in range(N)])
    cut = rounding_f(N * 0.15)
    trimmed_opions = opinions[cut:N - cut]
    res = rounding_f(sum(trimmed_opions) / len(trimmed_opions))
    print(res)
    