# 분할정복, 재귀 
n, r, c = map(int, input().split())

def go(n, r, c):
    if n == 1:
        return 2*r + c
    else:
        # 2^n*2^n배열부터 4등분씩 해가면서 r,c의 위치를 0,1,2,3에 따라 나누며 찾는다
        # 4등분 했을때 r,c가 0(좌상)의 위치인 경우
        if r < 2**(n-1) and c < 2**(n-1):
            return go(n-1, r, c)
        # 4등분 했을때 r,c가 1(우상)의 위치인 경우
        elif r < 2**(n-1) and c >= 2**(n-1):
            return go(n-1, r, c-2**(n-1)) + 2**(2*n-2)
        # 2의 위치(좌하)
        elif r >= 2**(n-1) and c < 2**(n-1):
            return go(n-1, r-2**(n-1), c) + (2**(2*n-2))*2
        # 3의 위치(우하)
        else:
            return go(n-1, r-2**(n-1), c-2**(n-1)) + (2**(2*n-2))*3

print(go(n, r, c))