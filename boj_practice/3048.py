# 구현(시뮬레이션 문제) 다시풀것!!
n1, n2 = map(int, input().split())
first = [{'direction': 1, 'name': ant} for ant in input()][::-1]
second = [{'direction': 2, 'name': ant} for ant in input()]
ants = first + second
t = int(input())

for __ in range(t):
    i = 0
    while i < len(ants) - 1:
        if ants[i]['direction'] < ants[i+1]['direction']:
            ants[i], ants[i+1] = ants[i+1], ants[i]
            i += 1
        i += 1
print("".join([ant['name'] for ant in ants])) 