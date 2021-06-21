# sw 역량 테스트 준비 - 기초 
n = int(input())
a = list(map(int, input().split()))
op = list(map(int, input().split()))

ans = []

def go(a, index, cur, plus, minus, mul, div):
    global ans

    if index == len(a):
        ans.append(cur)
        return
    
    if plus > 0:
        go(a, index+1, cur+a[index], plus-1, minus, mul, div)
    if minus > 0:
        go(a, index+1, cur-a[index], plus, minus-1, mul, div)
    if mul > 0:  
        go(a, index+1, cur*a[index], plus, minus, mul-1, div)
    if div > 0:
        go(a, index+1, cur//a[index] if cur > 0 else -((-cur)//a[index]), plus, minus, mul, div-1)

go(a, 1, a[0], op[0], op[1], op[2], op[3])
ans.sort()
print(ans[-1])
print(ans[0])