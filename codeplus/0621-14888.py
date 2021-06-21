# sw 역량 테스트 준비 - 기초 
n = int(input())
a = list(map(int, input().split()))
op = list(map(int, input().split()))

ans_max = -1e8
ans_min = 1e8

def go(a, index, cur, plus, minus, mul, div):
    global ans_max, ans_min

    if index == len(a):
        if plus < 0 or minus < 0 or mul < 0 or div < 0:
            return
        if ans_max < cur:
            ans_max = cur
        if ans_min > cur:
            ans_min = cur
        return
    
    go(a, index+1, cur+a[index], plus-1, minus, mul, div)
    go(a, index+1, cur-a[index], plus, minus-1, mul, div)
    go(a, index+1, cur*a[index], plus, minus, mul-1, div)
    go(a, index+1, cur//a[index] if cur > 0 else -((-cur)//a[index]), plus, minus, mul, div-1)

go(a, 1, a[0], op[0], op[1], op[2], op[3])
print(ans_max)
print(ans_min)