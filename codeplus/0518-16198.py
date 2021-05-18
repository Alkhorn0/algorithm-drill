# brute force, recursive
# go의 파라미터를 w 하나로만 하고 
# energy값을 갱신하며 더해가는 방식으로도 가능
def go(index, w, energy):
    global ans
    if index == 2:
        return
    i = len(w)
    for x in range(1, i-1):
        e = w[x-1]*w[x+1]
        ans.append(energy + e)
        nw = w[:x]+w[x+1:]
        go(index-1, nw, energy+e)

n = int(input())
w = list(map(int, input().split()))
ans = []
go(len(w), w, 0)
ans.sort()
print(ans[-1])