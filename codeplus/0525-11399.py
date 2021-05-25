# greedy, sorting
n = int(input())
p = sorted(list(map(int, input().split())))
t = []
for i in range(n):
    t.append(sum(p[:i+1]))
print(sum(t))