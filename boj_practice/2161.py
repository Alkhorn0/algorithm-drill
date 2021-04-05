n = int(input())
deck = [i for i in range(1, n+1)]

while len(deck)>1:
    print(deck.pop(0), end=' ')
    k = deck.pop(0)
    deck.append(k)
print(deck[0])