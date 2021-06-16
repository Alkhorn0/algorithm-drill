# sw 역량 테스트 준비 - 기초
def next_permutation(a):
    i = len(a)-1
    while i >= 0 and a[i] <= a[i-1]:
        i -= 1
    if i <= 0:
        return False
    j = len(a)-1
    while a[j] <= a[i-1]:
        j -= 1
    a[i-1], a[j] = a[j], a[i-1]
    j = len(a)-1
    while i < j:
        a[i], a[j] = a[j], a[i]
        i += 1
        j -= 1
    return True

def cal(a):
    res = 0
    for i in range(len(a)-1):
        res += abs(a[i]-a[i+1])
    return res

n = int(input())
a = sorted(list(map(int, input().split())))
ans = cal(a)
while next_permutation(a):
    temp = cal(a)
    if ans < temp:
        ans = temp
print(ans)