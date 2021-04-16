# 완전 탐색 문제
from itertools import permutations
dwarfs = []
answer = []
for _ in range(9):
    dwarfs.append(int(input()))
possible = list(permutations(dwarfs,7))
for i in possible:
    s = sum(i)
    if s == 100:
        answer = sorted(i)
        break
for i in answer:
    print(i)