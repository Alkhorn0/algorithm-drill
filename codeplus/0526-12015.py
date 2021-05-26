# greedy, bisect
# 수열을 하나하나 탐색하면서 부분수열을 구한다, 이때 부분수열을 저장하는 배열로 
# d를 사용, 수열의 요소인 i가 d[-1]보다 크면 추가해주고, 작은 경우 d를 
# 이분탐색하여 i보다 작은 수 중에서 가장 큰 수와 i를 교환해준다. 
# 단, 이것은 배열의 길이가 아닌 배열자체를 구하는 문제에서는 오답이 된다
# 수열의 순서를 지키지 않기 때문 
# (ex) 5671의 경우 원래는 567이 답이지만 이 풀이라면 167이 되어버린다)
# (이를 해결하기 위해선 추가로 배열을 사용해 인덱스를 기록해줌으로 해결가능)
import sys
from bisect import bisect_left
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
d = [0]

for i in a:
    if d[-1] < i:
        d.append(i)
    else:
        # i보다 작은 d의 요소의 인덱스를 반환 -> bisect_left
        d[bisect_left(d, i)] = i
print(len(d)-1)
