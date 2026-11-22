class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def create_tree():
    value = input("Enter node data (-1 for no node): ")
    if value == "-1":
        return None

    node = Node(value)
    print("Enter left child of", value)
    node.left = create_tree()
    print("Enter right child of", value)
    node.right = create_tree()
    return node

def inorder(root):
    if root is None:
        return
    inorder(root.left)
    print(root.data, end=" ")
    inorder(root.right)

def preorder(root):
    if root is None:
        return
    print(root.data, end=" ")
    preorder(root.left)
    preorder(root.right)

def postorder(root):
    if root is None:
        return
    postorder(root.left)
    postorder(root.right)
    print(root.data, end=" ")

def main():
    print("Create Binary Tree")
    root = create_tree()

    print("\\nInorder Traversal:")
    inorder(root)
    print("\\nPreorder Traversal:")
    preorder(root)
    print("\\nPostorder Traversal:")
    postorder(root)
    print()

if __name__ == "__main__":
    main()
