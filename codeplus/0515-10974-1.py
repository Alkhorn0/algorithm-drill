# brute force, permutation
# 순열을 재귀함수로 나타내기
n = int(input())
a = [0]*n
visited = [False]*(n+1)
def permutation(index, n):
    if index == n:
        print(' '.join(map(str, a)))
        return
    for i in range(1, n+1):
        if visited[i]:
            continue
        a[index] = i
        visited[i] = True
        permutation(index+1, n)
        visited[i] = False
permutation(0, n)