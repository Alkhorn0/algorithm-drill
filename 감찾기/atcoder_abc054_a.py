a, b = map(int, input().split())

rank = [2,3,4,5,6,7,8,9,10,11,12,13,1]
rank_a, rank_b = 0, 0
for i in range(13):
    if a == rank[i]:
        rank_a = i
    if b == rank[i]:
        rank_b = i

if rank_a == rank_b:
    print('Draw')
elif rank_a > rank_b:
    print('Alice')
else:
    print('Bob')