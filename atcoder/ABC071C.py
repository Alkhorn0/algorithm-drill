n = int(input())
a = sorted(list(map(int, input().split())))
answer = 1
cnt = 0
i = n - 1

while i >= 0:
    if a[i] == a[i - 1]:
        answer *= a[i]
        cnt += 1
        i -= 2
    else:
        i -= 1
    
    if cnt >= 2:
        break
if cnt >= 2:
    print(answer)
else:
    print(0)


