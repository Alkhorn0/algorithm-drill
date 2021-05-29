# sorting
import sys
input = sys.stdin.readline

n = int(input())
a = []
for i in range(n):
    age, name = input().split()
    b = [int(age), name, i]
    a.append(b)
a.sort(key=lambda x:x[2])
a.sort(key=lambda x:x[0])
for i in a:
    print(i[0], i[1])