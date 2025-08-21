import sys
input = sys.stdin.readline

n, m = map(int, input().split())

site_dic = {}

for _ in range(n):
    address, pw = input().split()
    site_dic[address] = pw

for _ in range(m):
    address = input().strip()
    print(site_dic[address])