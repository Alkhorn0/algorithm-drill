# 트리 만드는 법에 대해 숙지할것 (다시보기)
# 프리오더, 인오더, 포스트오더의 차이점 숙지
class Node:
    def __init__(self, left, right):
        self.left = left
        self.right = right
a = dict()
A = ord('A')
def preorder(x):
    if x == -1:
        return
    print(chr(x+A), end='')
    preorder(a[x].left)
    preorder(a[x].right)
def inorder(x):
    if x == -1:
        return
    inorder(a[x].left)
    print(chr(x+A), end='')
    inorder(a[x].right)
def postorder(x):
    if x == -1:
        return
    postorder(a[x].left)
    postorder(a[x].right)
    print(chr(x+A), end='')

n = int(input())
for _ in range(n):
    x, y, z = input().split()
    x = ord(x) - A
    left = -1
    right = -1
    if y != '.':
        left = ord(y) - A
    if z != '.':
        right = ord(z) - A
    a[x] = Node(left, right)
preorder(0)
print()
inorder(0)
print()
postorder(0)