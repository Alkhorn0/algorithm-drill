T = int(input())
for t in range(1,T+1):
    n, m, l = map(int, input().split())
    numbers = list(map(int, input().split()))
    for _ in range(m):
        command = list(input().split())
        order = command[0]
        if order == 'I' or order == 'C':
            index = int(command[1])
            num = int(command[2])
            if order == 'I':
                new_numbers = numbers[:index]
                new_numbers.append(num)
                new_numbers += numbers[index:]
                numbers = new_numbers
            elif order == 'C':
                numbers[index] = num
        elif order == 'D':
            index = int(command[1])
            new_numbers = numbers[:index]+numbers[index+1:]
            numbers = new_numbers
    if l >= len(numbers):
        print(f'#{t} {-1}')
    else:
        print(f'#{t} {numbers[l]}')

