# 그리디
n, l = map(int, input().split())
leak = list(map(int, input().split()))
leak.sort()
start = leak[0]
end = leak[0] + l
cnt = 1

for i in range(n):
    if start <= leak[i] < end:
        continue
    else:
        start = leak[i]
        end = leak[i] + l
        cnt += 1
print(cnt)