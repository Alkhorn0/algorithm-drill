# greedy
# s->t를 만드는 문제이지만 
# t->s를 만들도록 역으로 연산하는게 더 쉽다
# 왜냐하면 가장 뒤쪽의 요소만 보면 어떤 연산을 했는지 알 수 있기 때문
# 따라서 t에 계속해서 연산을 하여 s와 크기가 같아질때까지 진행해주고
# 그렇게 나온 t'가 s와 같은지 판단하면 되는 문제

s = list(input())
t = list(input())
while len(t) > len(s):
    if t[-1] == 'A':
        t.pop()
    else:
        t.pop()
        t = t[::-1]
if s == t:
    print(1)
else:
    print(0)