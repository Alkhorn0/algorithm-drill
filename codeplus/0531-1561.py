# 다시보기

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
a = list(map(int, input().split()))

if n <= m:
    print(n)
    exit()

left = 0
right = 2000000000 * 10000
while left <= right:
    mid = (left+right)//2
    begin, end = 0, m
    for i in range(m):
        end += mid//a[i]
    begin = end
    for i in range(m):
        if mid%a[i]==0:
            begin -= 1
    begin += 1
    if n < begin:
        right = mid-1
    elif n > end:
        left = mid+1
    else:
        for i in range(m):
            if mid%a[i] == 0:
                if n == begin:
                    print(i+1)
                    exit()
                begin += 1
