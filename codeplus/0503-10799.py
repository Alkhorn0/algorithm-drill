# 자료구조, 스택(다시보기)
data = input()
stack = []
cnt = 0
ans = 0
for i in data:
    cnt += 1
    if i == '(':
       stack.append(cnt)
    elif i == ')':
        if stack[-1]+1 == cnt:
            stack.pop()
            ans += len(stack)
        else:
            stack.pop()
            ans += 1
print(ans)