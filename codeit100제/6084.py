h, b, c, s = map(int,input().split())

pcm = ((h*b*c*s/1024)/1024)/8
print("%.1f MB" %pcm)