# eval함수 -> str의 형태로 수식을 입력받아 계산해주는 함수
# 다시보기(eval안쓰고 풀기)

n = int(input())
a = list(input())
m = (n+1)//2 - 1
ans = None

for s in range(1<<m):
    ok = True
    for i in range(m-1):
        if (s&(1<<i)) > 0 and (s&(1<<(i+1))) > 0:
            ok = False
    if not ok:
        continue
    
    b = a[:]
    for i in range(m):
        if (s&(1<<i)) > 0:
            k = 2*i+1
            b[k-1] = '('+b[k-1]
            b[k+1] = b[k+1]+')'
    c = ''.join(b)
    tmp = eval(c)
    if ans is None or ans < tmp:
        ans = tmp
print(ans)