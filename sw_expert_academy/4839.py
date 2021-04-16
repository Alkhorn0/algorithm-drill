# 이진탐색 문제 
def binarySearch(p, key):
    start = 1
    end = p
    cnt = 0
    while start <= end:
        cnt += 1
        middle = start + (end-start)//2
        if key == middle:
            return cnt
        elif key < middle:
            end = middle
        else:
            start = middle
    return p+1 
T = int(input())
for t in range(1, T+1):
    p, a, b = map(int, input().split())
    a_result = binarySearch(p, a)
    b_result = binarySearch(p, b)
    if a_result == b_result:
        print(f'#{t} 0')
    elif a_result < b_result:
        print(f'#{t} A')
    else:
        print(f'#{t} B')