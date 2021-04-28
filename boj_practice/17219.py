# 해시 및 집합
import sys
input = sys.stdin.readline
n, m = map(int, input().split())
storage = {}
for _ in range(n):
    site, password = input().split()
    storage[site] = password
for _ in range(m):
    find = input().rstrip()
    print(storage[find])
