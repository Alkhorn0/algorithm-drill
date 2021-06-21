# 다시보기
while True:
    # l -> 히스토그램의 높이 저장
    n, *l = list(map(int, input().split()))
    if n == 0:
        break
    s = []
    ans = 0
    # 마지막에 추가되는 히스토그램을 계산하기 위해 추가될 수 있는 가장 작은 값 대입
    l.append(0)
    # 하나씩 넣되, 이전에 추가된 히스토그램보다 높이가 낮은 히스토그램이 추가 될 경우
    # 추가할 높이보다 낮은 높이가 나올 때 까지 계산해준다.
    for i, h in enumerate(l):
        # 추가 될 높이가 낮을 경우 and s에 요소가 있는 경우
        while s and l[s[-1]] > h:
            height = l[s.pop()]
            if s:
                # 가장 최근에 추가된 히스토그램을 기준으로 왼편으로 하나씩 pop해가며 비교
                # 점차 높이는 낮아지고 너비는 넓어진다.
                width = i-s[-1]-1
            else:
                width = i
                
            if ans < width*height:
                ans = width*height
        
        s.append(i)
    print(ans)