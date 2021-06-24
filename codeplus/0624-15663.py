# sw 역량 테스트 준비 - 기초 
n, m = map(int, input().split())
a = sorted(list(map(int, input().split())))
t = [False]*n
ans = [0]*m
answer = []

def go(index, n, m):
    if index == m:
        answer.append(tuple(ans))
        return
    for i in range(n):
        if t[i]:
            continue
        t[i] = True
        ans[index] = a[i]
        go(index+1, n, m)
        t[i] = False

go(0, n, m)

answer = sorted(list(set(answer)))
for i in answer:
    print(' '.join(map(str, i)))