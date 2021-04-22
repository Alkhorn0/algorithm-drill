T = int(input())
for t in range(1, T+1):
    n, m, k = map(int, input().split())
    target = 0
    numbers = list(map(int, input().split()))

    for _ in range(k):
        target += m
        if target >= len(numbers):
            target %= len(numbers)
        add_number = numbers[target-1] + numbers[target]
        if target != 0: 
            new_numbers = numbers[:target] + [add_number] + numbers[target:]
            numbers = new_numbers
        else:
            numbers.append(add_number)
            target = -1
        
    print(f'#{t}',end=' ')
    for i in numbers[-1:-11:-1]:
        print(i,end=" ")
    print()

