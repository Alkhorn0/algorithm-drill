import sys
n = int(sys.stdin.readline())
mountain = list(map(int, sys.stdin.readline().split()))

s = 0
result = 0
cnt = 0
for i in mountain:
    if i > s:
        s = i
        cnt = 0
    else:
        cnt += 1
    result = max(result, cnt)

print(result)