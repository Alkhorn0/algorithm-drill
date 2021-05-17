def go(index, start, link):
    if index == n:
        if len(start) == 0:
            return -1
        if len(link) == 0:
            return -1
        t1 = 0
        t2 = 0
        for i in start:
            for j in start:
                if i == j:
                    continue
                t1 += s[i][j]
        for i in link:
            for j in link:
                if i == j:
                    continue
                t2 += s[i][j]
        dif = abs(t1-t2)
        return dif
    ans = -1
    # 값 갱신후 새로 저장하는 부분
    t1 = go(index+1, start+[index], link)
    if ans == -1 or (t1 != -1 and ans > t1):
        ans = t1
    t2 = go(index+1, start, link+[index])
    if ans == -1 or (t2 != -1 and ans > t2):
        ans = t2
    return ans

n = int(input())
s = [list(map(int, input().split())) for _ in range(n)]
print(go(0, [], []))