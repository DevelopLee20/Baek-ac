N = int(input())

tree = {}
for _ in range(N):
    parent, child1, child2 = map(str, input().split(" "))
    tree[parent] = [child1, child2]

def preorder(parent: str):
    if parent != ".":
        print(parent, end="")
        preorder(tree[parent][0])
        preorder(tree[parent][1])
    return

def inorder(parent: str):
    if parent != ".":
        inorder(tree[parent][0])
        print(parent, end="")
        inorder(tree[parent][1])
    return
    
def postorder(parent: str):
    if parent != ".":
        postorder(tree[parent][0])
        postorder(tree[parent][1])
        print(parent, end="")
    return

visited = []
preorder('A')
print()
visited = []
inorder('A')
print()
visited = []
postorder('A')
print()