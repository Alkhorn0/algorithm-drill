from collections import deque

# prime -> 소수인지 아닌지를 저장
prime = [True]*10001
# 에라토스테네스의 체(소수판별)
for i in range(2, 10001):
    if prime[i] == True:
        for j in range(i*i, 10001, i):
            prime[j] = False
# 숫자 변환
def change(num, index, digit):
    # index = 0 , digit = 0는 초기값 의미
    if index == 0 and digit == 0:
        return -1
    s = list(str(num))
    # 문자형으로 저장시키기 위함
    s[index] = chr(digit+ord('0'))
    # 다시 형변환
    return int(''.join(s))

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    # 방문 여부
    visited = [False]*10001
    # 메모이제이션
    d = [0]*10001
    d[n] = 0
    visited[n] = True
    q = deque()
    q.append(n)
    while q:
        x = q.popleft()
        for i in range(4):
            for j in range(10):
                y = change(x, i, j)
                if y != -1:
                    # 소수이면서 방문한적 없는경우 추가로 탐색
                    if prime[y] and visited[y] == False:
                        q.append(y)
                        d[y] = d[x]+1
                        visited[y] = True
    print(d[m])