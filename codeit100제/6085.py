w, h, b = map(int,input().split())

csl = ((w*h*b/1024)/1024)/8
print("%.2f MB" %csl)