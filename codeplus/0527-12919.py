# greedy, recursion
# s->t 가 아닌 t->s로 바꾸면서 확인
# 단, 'A'와 'B'를 확인해야하는 위치가 
# 다르기 때문에 함수에 넣어서 재귀로 돌린다
s = input()
t = input()
def go(s, t):
    if s == t:
        return True
    if len(t) > 0:
        # 한꺼번에 하는 이유 -> BA와 같이 t[-1] == 'A' 
        # / t[0] == 'B'를 동시에 성립하는 경우, 
        # 각각의 연산을하여 맞는게 있으면 답이 나오기 때문
        if t[-1] == 'A' and go(s, t[:-1]):
            return True
        if t[0] == 'B' and go(s, t[:0:-1]):
            return True
    return False
if go(s, t):
    print(1)
else:
    print(0)