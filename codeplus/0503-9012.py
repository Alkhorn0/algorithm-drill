# 자료구조, 스택
T = int(input())
for _ in range(T):
    stack = []
    string = list(input())
    judge = True
    for i in string:
        if i == '(':
            stack.append(i)
        elif i == ')':
            if stack:
                stack.pop()
            else:
                judge = False
                break
    if judge == False:
        print("NO")
    else:
        if stack:
            print("NO")
        else:
            print("YES")