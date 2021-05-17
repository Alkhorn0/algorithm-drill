# brute force, permutation
'''
다음 순열을 나타내기 위해서는 자릿수에 맞게 내림차순이 되어야함
1. i로 뒤에서 부터 가장 먼저나오는 내림차순의 시작점을 판단
2. i가 인덱스 0이라는 건 전체가 내림차순 == 가장 마지막 순열 -> 다음 순열 없음
3. i-1인덱스는 새롭게 뒤쪽으로 보낼 원소와 a[i-1] 보다 큰 원소의 인덱스 = j 교환을 위해 필요
4. a[i-1]과 a[j]가 교환된 후 새롭게 정렬을위해 새로이 가장 뒤쪽원소를 j로 새로 지정
5. 차례차례 교환하며 정렬
'''
def next_permutation(a):
    i = len(a)-1
    while i > 0 and a[i-1] >= a[i]:
        i -= 1
    if i <= 0:
        return False
    j = len(a) - 1
    while a[j] <= a[i-1]:
        j -= 1
    a[i-1], a[j] = a[j], a[i-1]
    j = len(a)-1
    while i < j:
        a[i], a[j] = a[j], a[i]
        i += 1
        j -= 1
    return True

n = int(input())
a = list(map(int, input().split()))
if next_permutation(a):
    print(' '.join(map(str, a)))
else:
    print(-1)