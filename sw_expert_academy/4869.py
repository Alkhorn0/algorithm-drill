def find(x):
    if x > n:
        return 0
    elif x == n:
        return 1
    return find(x + 10) + find(x + 20) * 2

T = int(input())
for t in range(1, T+1):
    n = int(input())
    answer = find(0)
    print(f'#{t} {answer}')