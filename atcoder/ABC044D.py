# 다시보기 
def check(b, n):
    res = 0
    while b <= n:
        res += n%b
        n = n // b
    res += n
    return res

n = int(input())
s = int(input())
start = 2
end = n
judge = False
answer = 0
while start <= end:
    if check(start, n) == s:
        answer = start
        judge = True
        break
    start += 1

if judge:
    print(answer)
else:
    print(-1)