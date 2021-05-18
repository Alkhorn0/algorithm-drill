def solve(a, index, save, plus, minus, mul, div):
    global ans
    if index == len(a):
        ans.append(save)
        return
    if plus > 0:
        solve(a, index+1, save+a[index], plus-1, minus, mul, div)
    if minus > 0:
        solve(a, index+1, save-a[index], plus, minus-1, mul, div)
    if mul > 0:
        solve(a, index+1, save*a[index], plus, minus, mul-1, div)
    if div > 0:
        if save < 0:
            solve(a, index+1, -((-save)//a[index]), plus, minus, mul, div-1)
        else:
            solve(a, index+1, save//a[index], plus, minus, mul, div-1)

n = int(input())
a = list(map(int, input().split()))
plus, minus, mul, div = map(int, input().split())
ans = []
solve(a, 1, a[0], plus, minus, mul, div)
ans.sort()
print(ans[-1])
print(ans[0])