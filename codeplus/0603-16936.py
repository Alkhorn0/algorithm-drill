# brute force
n = int(input())
b = list(map(int, input().split()))
mul3 = []
div2 = []
check = [False]*len(b)
x = 0
for i in range(len(b)):
    m = b[i]*3
    d = b[i]//2 if b[i]%2 == 0 else -1
    mul3.append(m)
    div2.append(d)
    if m not in b and d not in b:
        x = b[i]
        check[i] = True
a = [x]
while n > 0:
    for i in range(len(b)):
        if check[i]:
            continue
        if a[-1] == mul3[i] or a[-1] == div2[i]:
            a.append(b[i])
            check[i] = True
            break
    n -= 1
print(' '.join(map(str, a)))

'''
다른 풀이
# 정수론, 정렬
# 소인수분해를 했을때, 가지고있는 3의 개수로 쉽게 순서를 구할 수 있음
# 왜냐하면 나3 연산은 가지고있는 3의 개수를 줄이기만 하기 때문 
# -> 소인수분해를 했을때 3의 개수가 가장 많은 수가 시작 수인 x가됨
# 이후 같은 3의 갯수를 가진 수들을 2의개수에 대해 오름차순으로 나열하면
# 수열 a가 된다

n = int(input())
a = list(map(int, input().split()))
for i in range(n):
    num = a[i]
    cnt = 0
    # 3의 개수에대해 내림차순정렬하고, 2의 개수에대해 오름차순 정렬을 해야함
    # 때문에 3의 개수를 cnt로세서 -cnt를 포함시킨다.
    while num%3 == 0:
        num = num//3
        cnt += 1
    a[i] = (-cnt, a[i])
# 정렬시키면 3의 개수에 대해 내림차순으로 정렬됨
a.sort()
ans = [x[1] for x in a]
print(*ans, sep=' ')
'''
