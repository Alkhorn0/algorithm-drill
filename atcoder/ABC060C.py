n, t = map(int, input().split())
t_i = list(map(int, input().split()))
answer = 0
for i in range(n-1):
    tmp = t_i[i+1] - t_i[i]
    if tmp <= t:
        answer += tmp
    else:
        answer += t
answer += t
print(answer)