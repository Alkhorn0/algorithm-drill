import sys
input = sys.stdin.readline

n, m = map(int, input().split())
name = set()
for _ in range(n):
    name.add(input().rstrip())
ans = []
for _ in range(m):
    x = input().rstrip()
    if x in name:
        ans.append(x)
ans.sort()
print(len(ans))
for i in ans:
    print(i)