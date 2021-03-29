n = int(input())
l = list(map(int,input().split(' ')))

l = sorted(l)
alice_sum = 0
bob_sum = 0
for i in range(n-1,-1,-2):
    alice_sum += l[i]
for j in range(n-2, -1, -2):
    bob_sum += l[j]
print(alice_sum - bob_sum)