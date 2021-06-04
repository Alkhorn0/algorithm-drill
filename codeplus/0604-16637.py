# 다시풀기
# 연산자와 숫자를 나누어 배치하는 것도 가능할듯

n = int(input())
a = list(input())
# a의 홀수번째 요소들만 숫자
for i in range(0, n, 2):
    a[i] = int(a[i])
# 연산자 개수
m = (n-1)//2
ans = None
# 모든 경우의 수 탐색
for s in range(1<<m):
    # 괄호 배치 가능
    ok = True
    for i in range(m-1):
        # 중첩괄호는 불가하다-> 연속한 연산자에 괄호배치하면 중첩괄호됨
        if (s&(1<<i)) > 0 and (s&(1<<(i+1))) > 0:
            ok = False
    # 괄호배치가 불가능한 경우는 생각하지 않는다
    if not ok:
        continue
    # a의 요소 복사
    b = a[:]
    for i in range(m):
        # 괄호가 배치된 경우 미리 계산
        if (s & (1<<i)) > 0:
            k = 2*i+1
            if b[k] == '+':
                b[k-1] += b[k+1]
                b[k+1] = 0
            elif b[k] == '-':
                b[k-1] -= b[k+1]
                b[k] = '+'
                b[k+1] = 0
            elif b[k] == '*':
                b[k-1] *= b[k+1]
                b[k] = '+'
                b[k+1] = 0
    # 식을 계산한 값 임시 저장
    tmp = b[0]
    for i in range(m):
        k = 2*i+1
        if b[k] == '+':
            tmp += b[k+1]
        elif b[k] == '-':
            tmp -= b[k+1]
        elif b[k] == '*':
            tmp *= b[k+1]
    if ans is None or ans < tmp:
        ans = tmp
print(ans)