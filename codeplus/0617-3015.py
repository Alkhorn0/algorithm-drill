# 다시보기
# 앞에서부터 한명씩 키를 추가하면서 키를 비교한다. 더 큰 사람이 추가될 경우
# 그 사람보다 작은 사람들은 뒷사람을 볼 수 없기 때문에 stack에서 pop해준다.
# 단, 키가 같은 사람이 연속해서 나올 경우, 그들끼리는 볼 수 있기때문에,
# 쌍의 수를 추가하기 위해 같은 키를 가지는 사람이 연속해서 나오는 경우를 계산하기 위한
# 리스트 c에 정보를 담아 이것으로 계산한다.

import sys
input = sys.stdin.readline
n = int(input().rstrip())
a = [int(input().rstrip()) for _ in range(n)]
stack = []
# 같은 키의 사람이 연속해서 나오는 경우를 제외하면 대부분 1의 값을 가진다.
c = []
ans = 0
for i in range(n):
    cnt = 1
    while stack:
        # 처음에 같은 키의 사람끼리는 서로 볼 수있다는 것을 간과해 틀림
        # c에 추가로 정보를 넣어 계산해준다.
        if stack[-1] <= a[i]:
            ans += c[-1]
            # 같은 경우 cnt를 통해 중첩시켜준다. (쌍의 수를 세기 위해)
            # ex) 키가 2인 사람 3명이 연달아 나올경우 -> s = [2,2,2,4]
            # c = [1,2,3,1] -> 이 되어 2,3,1 순으로 ans에 더해진다.
            if stack[-1] == a[i]:
                cnt += c[-1]
            # 계산 될 때마다 pop으로 제외해줌 -> stack은 결국 내림차순으로 남음
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