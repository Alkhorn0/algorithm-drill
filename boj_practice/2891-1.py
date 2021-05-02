# greedy
n, s, r = map(int, input().split())
broken = list(map(int, input().split()))
rent = list(map(int, input().split()))

for i in rent:
    for j in broken:
        if i == j or i+1 == j or i-1 == j:
            broken.remove(j)
            continue
print(len(broken)) 