# 시뮬레이션 문제
N, m, M, t, r = map(int, input().split())
heart_beat = m
time = 0
workout = 0

if heart_beat > M or heart_beat + t > M:
    print(-1)
else: 
    while True:
        if workout == N:
            print(time)
            break
        else:
            time += 1
            if heart_beat + t <= M:
                workout += 1
                heart_beat += t
            else:
                if heart_beat - r < m:
                    heart_beat = m
                else:
                    heart_beat -= r


