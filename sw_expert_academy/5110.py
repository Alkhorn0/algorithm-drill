T = int(input())
for t in range(1, T+1):
    n, m = map(int, input().split())
    numbers = []
    for i in range(m):
        if i == 0:
            numbers = list(map(int, input().split()))
        else:
            nums = list(map(int, input().split()))
            for j in range(len(numbers)):
                if numbers[j] > nums[0]:
                    numbers[j:j] = nums
                    break
                elif j == len(numbers)-1:
                    numbers += nums
    print(f"#{t}",end=" ")
    for k in numbers[-1:-11:-1]:
        print(k,end=' ')
    print()