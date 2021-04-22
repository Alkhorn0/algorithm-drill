T = int(input())
for t in range(1, T+1):
    n, m, l = map(int, input().split())
    numbers = list(map(int, input().split()))
    for _ in range(m):
        index, num = map(int, input().split())
        new_numbers = numbers[:index] + [num] + numbers[index:]
        numbers = new_numbers
    print(f'#{t} {numbers[l]}')