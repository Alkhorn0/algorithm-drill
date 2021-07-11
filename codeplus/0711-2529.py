# sw 역량 테스트 준비 - 기초 
def check(x, y, op):
    if op == '<':
        if x > y:
            return False
    elif op == '>':
        if x < y:
            return False
    return True

def go(index, n):
    if index == k+1:
        ans.append(n)
        return
    for i in range(10):
        if visited[i]:
            continue
        if index == 0 or check(n[-1], str(i), a[index-1]):
            visited[i] = True
            go(index+1, n+str(i))
            visited[i] = False

k = int(input())
a = input().split()
visited = [False]*10
ans = []
go(0, '')
ans.sort()
print(ans[-1])
print(ans[0])