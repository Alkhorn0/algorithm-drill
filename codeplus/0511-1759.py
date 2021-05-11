# 브루트포스, 재귀
l, c = map(int, input().split())
word = sorted(list(input().split()))
visited = [False]*c
a = [0]*l

def pos(index, start, l, c):
    if index == l:
        cnt = 0
        for i in ['a', 'i', 'o', 'u', 'e']:
            if i in a:
                cnt += 1
        if cnt < 1:
            return
        elif len(a) - cnt < 2:
            return
        print(''.join(map(str, a)))
        return 
    for i in range(start, c):
        if visited[i]:
            continue
        start = i+1
        visited[i] = True
        a[index] = word[i]
        pos(index+1, start, l, c)
        visited[i] = False

pos(0, 0, l, c)

# 다른 풀이
def check(password):
    ja = 0
    mo = 0
    for x in password:
        if x in 'aioue':
            mo += 1
        else:
            ja += 1
    return ja >= 2 and mo >= 1

def go(n, alpha, password, i):
    if len(password) == n:
        if check(password):
            print(password)
        return
    if i == len(alpha):
        return
    go(n, alpha, password+alpha[i], i+1)
    go(n, alpha, password, i+1)

n, m = map(int, input().split())
a = sorted(input().split())
go(n, a, "", 0)