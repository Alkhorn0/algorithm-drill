# 이분탐색, sorting, 분할정복
import sys, bisect
input = sys.stdin.readline

n = int(input())
cards = sorted(list(map(int, input().split())))
m = int(input())
l = list(map(int, input().split()))

for i in l:
    print(abs(bisect.bisect_left(cards, i)-bisect.bisect_right(cards, i)),end=' ')