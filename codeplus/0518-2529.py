# brute force, recursive

def check(x, y, op):
    if op == '<':
        if x > y:
            return False
    elif op == '>':
        if x < y:
            return False
    return True

def go(index, num):
    if index == k+1:
        ans.append(num)
        return
    for i in range(10):
        if visited[i]:
            continue
        if index == 0 or check(num[-1], str(i), a[index-1]):
            visited[i] = True
            go(index+1, num+str(i)) 
            visited[i] = False

k = int(input())
a = input().split()
visited = [False]*10
ans = []
go(0, '')
ans.sort()
print(ans[-1])
print(ans[0])
