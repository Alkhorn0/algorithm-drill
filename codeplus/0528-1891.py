# 분할정복
# 출발할 사분면을 좌표로 나타낸후 좌표이동을 통해 
# 이동시킨뒤 사분면의 형태로 치환한다
d, n = input().split()
d = int(d)
x, y = map(int, input().split())
# 이동시킬 사분면 좌표로 치환
def go(d, n):
    x, y = 0, 0
    for i in n:
        if i == '1':
            x += 0
            y += 2**(d-1)
        elif i == '2':
            x += 0
            y += 0
        elif i == '3':
            x += 2**(d-1)
            y += 0
        else:
            x += 2**(d-1)
            y += 2**(d-1)
        d -= 1
    return x, y
# 좌표이동
a, b = go(d, n)
a -= y
b += x
#print(a, b)
# 좌표 -> 사분면형태
def gogo(a, b, d):
    if a < 0 or a >= 2**d or b < 0 or b >= 2**d:
        return -1
    ans = ''
    while d > 0:
        # 나머지로 나오는 수를 기준으로 치환해 나가므로 순서가 거꾸로 된다
        # 마지막에 반전시켜 반환시키면 됨
        x = a%2
        y = b%2
        if x == 0 and y == 0:
            ans += '2'
        elif x == 0 and y == 1:
            ans += '1'
        elif x == 1 and y == 0:
            ans += '3'
        else:
            ans += '4'
        a //= 2
        b //= 2
        d -= 1
        #print(a, b)
    return ans[::-1]
print(gogo(a, b, d))  