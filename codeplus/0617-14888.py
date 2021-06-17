# sw 역량 테스트 준비 - 기초 
def next_permutation(o):
    i = len(o)-1
    while i > 0 and o[i] <= o[i-1]:
        i -= 1
    if i <= 0:
        return False
    j = len(o)-1
    while o[j] <= o[i-1]:
        j -= 1
    o[i-1], o[j] = o[j], o[i-1]
    j = len(o)-1
    while i < j:
        o[i], o[j] = o[j], o[i]
        i += 1
        j -= 1
    return True

def cal(a, o):
    res = a[0]
    for i in range(len(o)):
        if o[i] == 0:
            res += a[i+1]
        elif o[i] == 1:
            res -= a[i+1]
        elif o[i] == 2:
            res *= a[i+1]
        else:
            if res < 0:
                res = -(-(res)//a[i+1])
            else:
                res //= a[i+1]
    return res

n = int(input())
a = list(map(int, input().split()))
op = list(map(int, input().split()))
o = []
for i in range(4):
    for _ in range(op[i]):
        o.append(i)

ans_min = ans_max = cal(a, o)
while next_permutation(o):
    temp = cal(a, o)
    if ans_min > temp:
        ans_min = temp
    if ans_max < temp:
        ans_max = temp
print(ans_max)
print(ans_min) 