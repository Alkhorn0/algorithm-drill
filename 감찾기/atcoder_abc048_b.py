a,b,x = map(int, input().split())

def f(n):
    if n == -1:
        return 0
    else:
        return n//x+1

print(f(b)-f(a-1))