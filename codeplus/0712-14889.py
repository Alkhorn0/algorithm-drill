# sw 역량 테스트 준비 - 기초 
def go(index, start, link):
    if index == n:
        if len(start) != n//2:
            return -1
        if len(link) != n//2:
            return -1
        t1 = 0
        t2 = 0
        for i in range(n//2):
            for j in range(n//2):
                if i == j:
                    continue
                t1 += s[start[i]][start[j]]
                t2 += s[link[i]][link[j]]
        diff = abs(t1-t2)
        return diff
    if len(start) > n//2:
        return -1
    if len(link) > n//2:
        return -1
    ans = -1
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