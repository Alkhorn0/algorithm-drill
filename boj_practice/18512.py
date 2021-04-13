# 완전 탐색 문제
x, y, p1, p2 = map(int,input().split())
runx = set(range(p1, 10**6, x))
runy = set(range(p2, 10**6, y))

r = runx&runy
print(min(r) if r else -1)
