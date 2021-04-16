# 완전 탐색 문제
nums = sorted(list(map(int, input().split())))

n = nums[2]*nums[3]*nums[4]

for i in range(nums[0], n+1):
    cnt = 0
    for j in nums:
        if i % j == 0:
            cnt += 1
    if cnt >= 3:
        print(i)
        break