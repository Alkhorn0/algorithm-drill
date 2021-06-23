# Binary Search Tree
# dictionary 가 아닌 set 도 가능
import sys
input = sys.stdin.readline

n = int(input())
log = {}
for _ in range(n):
    name, status = input().split()
    if status == 'enter':
        log[name] = status
    else:
        del log[name]

log = sorted(list(log))
for i in log[::-1]:
    print(i)
