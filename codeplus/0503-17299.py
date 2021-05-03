# 자료구조, 스택
n = int(input())
a = list(map(int, input().split()))
f = [0]*(max(a)+1)
s = []
ans = [0]*n
for i in a:
    f[i] += 1
for j in range(n):
    if not s:       # 스택이 비어있는 경우 일단 저장(a[j]의 오등큰수 x)
        s.append(j)
    while s and f[a[s[-1]]] < f[a[j]]:
        ans[s.pop()] = a[j] # 스택의 top과 비교 하면서 오등큰수에 해당하면 넣어줌
    s.append(j)     # a[j]의 오등큰수를 못찾았으므로 추가해줌
while s:    # 한번 돌고 아직 스택에 남아있으면 ngf(i)=-1
    ans[s.pop()] = -1
print(' '.join(map(str, ans)))