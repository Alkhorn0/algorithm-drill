# sw 역량 테스트 준비 - 기초 
def go(a, result, index):
    global ans
    if index == n:
        if sum(result) == s and result != []:
            ans += 1
        return
    go(a, result+[a[index]], index+1)
    go(a, result, index+1)

n, s = map(int, input().split())
a = list(map(int, input().split()))
ans = 0

go(a, [], 0)
print(ans)