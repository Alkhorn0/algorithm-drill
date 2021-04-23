def find(info, n, answer):
    for i in range(e):
        if info[i*2] == n:
            new = info[i*2+1]
            answer = find(info, new,answer)
            answer += 1
    return answer
T = int(input())
for t in range(1, T+1):
    e, n = map(int, input().split())
    info = list(map(int, input().split()))
    answer = 1
    print(f'#{t} {find(info, n, answer)}')

        