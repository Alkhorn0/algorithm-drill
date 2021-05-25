from collections import deque
# 숫자가 작아지는 연산('-' or '/')의 경우 0 혹은 1이되어 
# 한번이상 쓸 일이 없기때문에 s->t로 할 때 10^9를 넘기는 
# 숫자를 활용할 일은 없음 -> 때문에 limit = 10^9
limit = 1000000000
s, t = map(int, input().split())
# 배열의 크기를 10^9로 만들면 메모리초과
check = set()
# bfs
q = deque()
q.append((s, ''))
check.add(s)
while q:
    x, s = q.popleft()
    # 조작의 종료조건
    if x == t:
        if len(s) == 0:
            s = '0'
        print(s)
        exit()
    # 나온적 없는 숫자의 경우 큐에 추가
    if 0 <= x*x <= limit and x*x not in check:
        q.append((x*x, s+'*'))
        check.add(x*x)
    if 0 <= x+x <= limit and x+x not in check:
        q.append((x+x, s+'+'))
        check.add(x+x)
    if 0 <= x-x <= limit and x-x not in check:
        q.append((x-x, s+'-'))
        check.add(x-x)
    if x != 0 and 0 <= x//x <= limit and x//x not in check:
        q.append((x//x, s+'/'))
        check.add(x//x)
print(-1)