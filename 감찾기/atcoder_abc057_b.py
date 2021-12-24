n, m = map(int, input().split())
student = []
checkpoints = []
for _ in range(n):
    x, y = map(int, input().split())
    student.append((x, y))
for _ in range(m):
    x, y = map(int, input().split())
    checkpoints.append((x, y))
ans = []
for ai, bi in student:
    d = 10**9
    p = 0
    for i in range(len(checkpoints)):
        ci, di = checkpoints[i]
        man = abs(ai-ci)+abs(bi-di)
        if d > man:
            d = man
            p = i+1
    ans.append(p)

for i in ans:
    print(i)