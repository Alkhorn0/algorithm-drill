# 이분탐색, sorting, 분할정복
import sys
input = sys.stdin.readline

n = int(input())
cards = sorted(list(map(int, input().split())))
m = int(input())
l = list(map(int, input().split()))

def bisect(i):
    start = 0
    end = len(cards)-1
    while start <= end:
        mid = (start+end)//2
        if i == cards[mid]:
            return 1
        elif i < cards[mid]:
            end = mid-1
        elif i > cards[mid]:
            start = mid + 1
    return 0

for i in l:
    print(bisect(i),end=' ')