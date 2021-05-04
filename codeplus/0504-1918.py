# 자료구조, 스택, 후위표기식 
def precedence(ch):
    if ch == '(':
        return 0
    elif ch in '+-':
        return 1
    return 2

s = input()
stack = []
ans = ''
for ch in s:
    if ch.isalpha():
        ans += ch
    elif ch == '(':
        stack.append(ch)
    elif ch == ')':
        while stack:
            sta = stack.pop()
            if sta == '(':
                break
            ans += sta
    else:
        while stack and precedence(stack[-1]) >= precedence(ch):
            ans += stack.pop()
        stack.append(ch)
while stack:
    ans += stack.pop()
print(ans)
