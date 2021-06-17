# 다시보기
from collections import deque

# 입력받음
# 막대의 상태 저장
s = []
for i in range(3):
    temp = input().split()
    # 처음에 막대에 놓인 원판의 개수
    cnt = int(temp[0])
    # 막대에 원판이 있는 경우
    if cnt > 0:
        s.append(temp[1])
    # 막대에 원판이 없는 경우
    else:
        s.append('')
# 문제에서 주어진 원판 a,b,c의 개수
cnt = [0, 0, 0]
for i in range(3):
    for ch in s[i]:
        cnt[ord(ch)-ord('A')] += 1
# 원판이 이동했을 때의 가능한 막대의 모든 상태(튜플형태)와 
# 그 때의 최소 이동 횟수 
d = dict()
# 큐에 초기상태 대입
q = deque()
q.append(tuple(s))
# 초기상태의 경우 최소이동횟수는 0
d[tuple(s)] = 0
while q:
    x = q.popleft()
    # x = 이동 전 상태, y = 이동 후 상태
    # i, j -> 막대의 번호(0->'A', 1->'B', 2->'C')
    for i in range(3):
        for j in range(3):
            # i = j는 이동을 안하니까 제외
            if i == j:
                continue
            # 이동을 시켜야 할 곳에 원판이 없으면 이동불가
            if len(x[i]) == 0:
                continue
            # 이동 후 상태를 나타내기 위해 우선 이동 전 상태 복사
            y = list(x[:])
            # 막대 i에서 막대 j로 가장 위의 원판 이동시키는 시행을 나타냄
            # 막대 j로 이전 상태의 막대 i의 가장 위의 원판 이동
            y[j] = y[j] + x[i][-1]
            # 이동한 이후에는 막대 i에는 가장 위 원판 제거
            y[i] = y[i][:-1]
            # 새로운 상태로 고정
            y = tuple(y)
            # 이전에 나온 적 없는 형태의 경우에는 최소 이동횟수 저장해줌
            if y not in d:
                d[y] = d[x] + 1
                q.append(y)

# 문제의 목표는 막대와 원판이 같은 알파벳을 갖도록 해야함
# 그 경우의 각 막대에는 같은 알파벳의 원판이 배치 된다 
# ex) (입력) 3 'CBA'/ 0 ''/ 0 '' -> 1 'A'/ 1 'B'/ 1 'C'가 목표상태
# 이 상태를 만드는 경우를 ans(['A','B','C'] 위의 ex의 경우)에 저장
# ans와 같은 상태를 만들었을때의 최소이동횟수는 d[tuple(ans)]에 저장되어 있음
ans = ['', '', '']
for i in range(3):
    for j in range(cnt[i]):
        ans[i] += chr(ord('A')+i)
print(d[tuple(ans)])

#print(d)
#print(cnt)
#print(ans)