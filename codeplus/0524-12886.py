# 다시보기
import sys
sys.setrecursionlimit(1500*1500)
# 조작을 통해 나온적이 있는지 알아보기 위함-> 있으면 만들 수 있다
check = [[False]*1501 for _ in range(1501)]
a, b, c = map(int, input().split())
s = a+b+c
def go(x, y):
    if check[x][y]:
        return
    check[x][y] = True
    l = [x, y, s-x-y]
    for i in range(3):
        for j in range(3):
            # a,b,c 중에서 작은 것을 x 큰것을 y로 했을 때만 확인 나머지는 무시
            if l[i] < l[j]:
                t = [x, y, s-x-y]
                t[i] += l[i]
                t[j] -= l[i]
                go(t[0], t[1])
# 내용을 아무리 변화시켜도 전체 값의 변화는 없음
# 때문에 3으로 나눴을때 나누어 떨어지지 않으면 
# 같은 값으로 만들 수 없음
if s % 3 != 0:
    print(0)
else:
    go(a, b)
    if check[s//3][s//3]:
        print(1)
    else:
        print(0)