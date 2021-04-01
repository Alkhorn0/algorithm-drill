n = int(input())
ropes = []
for __ in range(n):
    rope = int(input())
    ropes.append(rope)

ropes = sorted(ropes)
max_weight = 0
for i in range(n):
    weight = (n-i)*ropes[i]
    max_weight = max(max_weight,weight)

print(max_weight)