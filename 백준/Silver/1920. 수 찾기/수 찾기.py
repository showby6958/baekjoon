import sys

N = int(sys.stdin.readline())
N_set = set(map(int, sys.stdin.readline().split()))

M = int(sys.stdin.readline())
M_lst = list(map(int, sys.stdin.readline().split()))


for m in M_lst:
    if m in N_set:
        print(1)
    else:
        print(0)