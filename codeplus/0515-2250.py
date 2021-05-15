# 다시 보기 
import sys
class node:
    def __init__(self):
        self.left = -1
        self.right = -1
        self.depth = 0
        self.order = 0
 
def inorder(node, depth):
    global order
    if node == -1:
        return
    inorder(a[node].left, depth+1)
    a[node].depth = depth
    order += 1
    a[node].order = order
    inorder(a[node].right, depth+1)
 
n = int(sys.stdin.readline())
a = [node() for _ in range(10001)]
left = [0]*10001
right = [0]*10001
parent = [0]*10001
order = 0
 
for i in range(n):
    x, b, c = map(int, sys.stdin.readline().split())
    a[x].left = b
    a[x].right = c
    if b != -1:
        parent[b]+=1
    if c != -1:
        parent[c]+=1
 
 
root = 0
for i in range(1, n+1):
    if parent[i] == 0:
        root = i
 
inorder(root, 1)
maxdepth = 0
for i in range(1, n+1):
    depth = a[i].depth
    order = a[i].order
    if left[depth] == 0:
        left[depth] = order
    else:
        left[depth] = min(left[depth], order)
    right[depth] = max(right[depth], order)
    maxdepth = max(maxdepth, depth)
 
maxwidth = 0
anslevel = 0
 
for i in range(1, maxdepth+1):
    if maxwidth < right[i] - left[i] + 1:
        maxwidth = right[i]-left[i]+1
        anslevel = i
 
sys.stdout.write("{} {}".format(anslevel, maxwidth))