a, b, c = map(int, input().split())

def pow(b):
    if b == 1:
        return a%c
    else:
        tmp = pow(b//2)
        if b%2 == 0:
            return tmp * tmp % c
        else:
            return tmp * tmp * a % c

print(pow(b))