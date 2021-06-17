# 다시보기
import sys
input = sys.stdin.readline
n = int(input().rstrip())
a = [int(input().rstrip()) for _ in range(n)]
stack = []
c = []
ans = 0
for i in range(n):
    cnt = 1
    while stack:
        if stack[-1] <= a[i]:
            ans += c[-1]
            if stack[-1] == a[i]:
                cnt += c[-1]
            stack.pop()
            c.pop()
        else:
            break
    if stack:
        ans += 1
    stack.append(a[i])
    c.append(cnt)

    #print(stack, ans, c)
print(ans)