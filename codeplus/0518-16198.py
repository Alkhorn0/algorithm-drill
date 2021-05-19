# brute force, recursive
# go의 파라미터를 w 하나로만 하고 
# energy값을 갱신하며 더해가는 방식으로도 가능
def go(index, w, energy):
    global ans
    if index == 2:
        return
    i = len(w)
    for x in range(1, i-1):
        e = w[x-1]*w[x+1]
        # 입력이 전부 양수이므로 에너지값을 끝까지 더한 값이 최댓값이됨 
        # 때문에 계산마다 값을 배열에 추가할 필요없이 중첩해서 더해줘도 됨
        ans.append(energy + e)
        # 슬라이싱으로 선택한 구슬 제거표현
        nw = w[:x]+w[x+1:]
        go(index-1, nw, energy+e)

n = int(input())
w = list(map(int, input().split()))
ans = []
go(len(w), w, 0)
ans.sort()
print(ans[-1])