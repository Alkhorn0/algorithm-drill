# 재귀 
n, A, B, C = map(int, input().split())
l = [int(input()) for _ in range(n)]
INF = 1e10

def go(index, a, b, c):
    if index == n:
        # 합성이외의 처리를 하는 경우 계산을 위해 막대 한개당 10을 빼고 절대값 처리 * 3
        # 각 막대를 만들기 위해 적어도 대나무 한개 이상은 들어가야하기 때문에 if문 작성
        return abs(a-A)+abs(b-B)+abs(c-C)-30 if min(a, b, c) > 0 else INF
    ret0 = go(index+1, a, b, c)
    ret1 = go(index+1, a+l[index], b, c) + 10
    ret2 = go(index+1, a, b+l[index], c) + 10
    ret3 = go(index+1, a, b, c+l[index]) + 10
    return min(ret0, ret1, ret2, ret3)

print(go(0, 0, 0, 0))