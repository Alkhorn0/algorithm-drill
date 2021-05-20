# 다시보기
# 각각의 단어에 대해 전부 검사하면 경우의 수가 너무 커지므로 
# 단어를 그대로가 아닌 그 단어를 구성하는 알파벳만을 비트마스크로 저장 (words)

# 배운 단어를 구성하는 알파벳(word) 와
# 전체 알파벳((1<<26)-1)에서 배운다고 가정한 알파벳(mask)을 빼준것을 
# & 연산하여 배우지 않은 알파벳이 단어에 있는 지를 검사하여 cnt값을 세준다
def count(mask, words):
    cnt = 0
    for word in words:
        if (word & ((1 << 26)-1-mask)) == 0:
            cnt += 1
    return cnt

# index는 검사하는 알파벳의 인덱스(ex) a->0)
# k는 배우는 앒파벳 k(입력으로 주어지는 값)
# mask는 index번째 알파벳을 배운다고 가정했을때의 배운 알파벳 저장(mask = 111이면 abc를 알고 있다고 가정)
# words는 입력으로 받은 단어에 포함된 알파벳 count함수에 넣기 위해 포함
def go(index, k, mask, words):
    # 잘못가정한 경우 
    # (입력으로 주어진 배우기로한 k의 수를 넘겨 배웠다고 가정한 경우 
    # 혹은 k가 5이하인 경우 
    # -> k가 5이하면 a,n,t,c,i중 한개 이상의 문자를 배우지 못함 ->
    # 단어의 시작인 anta와 끝인 tica 중 하나 이상을 읽지 못해 아무 단어도 읽을 수 없음)
    if k < 0:
        return 0
    # 문제 없이 끝까지 탐색한 경우 count함수로 보내 읽을 수 있는 단어를 파악
    if index == 26:
        return count(mask, words)
    ans = 0
    # index 번째 알파벳을 배운다고 가정 -> t1
    t1 = go(index+1, k-1, mask|(1<<index), words)
    if ans < t1:
        ans = t1
    # 만일 index번째 알파벳이 a,n,t,i,c 가 아닌 경우 안배울 수도 있기 때문에 그러한 경우를 가정 -> t2
    if index not in [ord('a')-ord('a'), ord('n')-ord('a'), ord('t')-ord('a'), ord('i')-ord('a'), ord('c')-ord('a')]:
        t2 = go(index+1, k, mask, words)
        if ans < t2:
            ans = t2
    return ans

n, k = map(int, input().split())
words = [0]*n
for i in range(n):
    s = input()
    for x in s:
        words[i] |= (1 << (ord(x)-ord('a')))
print(go(0, k, 0, words))