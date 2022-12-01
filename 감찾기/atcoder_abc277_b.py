n = int(input())
deck = []
ans = 'Yes'
for _ in range(n):
    s = input()
    if s[0] not in ['H','D','C','S'] or s[1] not in ['A','2','3','4','5','6','7','8','9','T','J','Q','K'] or s in deck:
        ans = 'No'
    deck.append(s)
print(ans)