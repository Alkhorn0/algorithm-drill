# 분할정복

d, n = input().split()
d = int(d)
x, y = map(int, input().split())

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

a, b = go(d, n)
a -= y
b += x
#print(a, b)
def gogo(a, b, d):
    if a < 0 or a >= 2**d or b < 0 or b >= 2**d:
        return -1
    ans = ''
    while d > 0:
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