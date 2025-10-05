class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None

def insert(root, val):
    if root is None:
        return Node(val)
    if val < root.data:
        root.left = insert(root.left, val)
    else:
        root.right = insert(root.right, val)
    return root

def inorder(root):
    if root:
        inorder(root.left)
        print(root.data, end=' ')
        inorder(root.right)

def search(root, key):
    if root is None:
        return False
    if root.data == key:
        return True
    elif key < root.data:
        return search(root.left, key)
    else:
        return search(root.right, key)

root = None
while True:
    print("\n1.Insert 2.Search 3.Display 4.Exit")
    ch = int(input("Enter choice: "))
    if ch == 1:
        root = insert(root, int(input("Enter value: ")))
    elif ch == 2:
        print("Found!" if search(root, int(input("Enter key: "))) else "Not Found!")
    elif ch == 3:
        print("Inorder Traversal: ", end='')
        inorder(root)
        print()
    elif ch == 4:
        break
