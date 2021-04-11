# 문자열, 스택 
while True:
    s = input()
    if s == ".":
        break
    stack = []
    possible = True
    for i in s:
        if i == '(' or i == '[':
            stack.append(i)
        elif i == ')':
            if stack == [] or stack[-1] == '[':
                possible = False
                break
            elif stack[-1] == '(':
                stack.pop()
        elif i == ']':
            if stack == [] or stack[-1] == '(':
                possible = False
                break
            elif stack[-1] == '[':
                stack.pop()
    if possible == True and stack == []:
        print('yes')
    else:
        print('no')