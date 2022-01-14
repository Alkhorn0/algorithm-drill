n, a, b = map(int, input().split())
h = [int(input()) for _ in range(n)]

def enough(t):
    tmp = t
    for i in range(n):
        if h[i] > t*b:
            tmp -= (h[i] - t*b - 1)//(a - b) + 1
        if tmp < 0:
            return False
    return True

def binary_search(left, right):
    for _ in range(70):
        mid = (left + right) // 2
        if enough(mid):
            right = mid
        else:
            left = mid
    return right

print(binary_search(0, 10**18))