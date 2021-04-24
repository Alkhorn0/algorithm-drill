from itertools import combinations

n, a = map(int, input().split())
cards = list(map(int, input().split()))
answer = 0
for i in range(1, n+1):
    possible = list(combinations(cards, i))
    for j in range(len(possible)):
        if sum(possible[j]) == a*i:
            answer += 1
print(answer)