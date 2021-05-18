def solve(index, num):
    if index == n:
        h[num] = 1
        return
    solve(index+1, num+s[index])
    solve(index+1, num)

n = int(input())
s = list(map(int, input().split()))
h = [0]*(2000001)
solve(0, 0)
for i in range(1, 2000001):
    if h[i] == 0:
        print(i)
        break
