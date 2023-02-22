N = int(input())

tree = {}

for i in range(N):
    root, left, right = input().split()
    tree[root] = [left, right]

def preorder(i):
    if i != '.':
        print(i, end="")
        preorder(tree[i][0])
        preorder(tree[i][1])

def inorder(i):
    if i != '.':
        inorder(tree[i][0])
        print(i, end="")
        inorder(tree[i][1])

def postorder(i):
    if i != '.':
        postorder(tree[i][0])
        postorder(tree[i][1])
        print(i, end="")

preorder("A")
print()
inorder("A")
print()
postorder("A")
print()