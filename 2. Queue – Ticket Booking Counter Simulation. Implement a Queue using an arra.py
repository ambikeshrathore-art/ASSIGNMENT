class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
 
 
class BinarySearchTree:
    def __init__(self):
        self.root = None
 
    def insert(self, root, data):
        if root is None:
            return Node(data)
 
        if data < root.data:
            root.left = self.insert(root.left, data)
        elif data > root.data:
            root.right = self.insert(root.right, data)
        else:
            print("Duplicate value not inserted.")
 
        return root
 
    def inorder_non_recursive(self):
        stack = []
        current = self.root
 
        while current is not None or stack:
            while current is not None:
                stack.append(current)
                current = current.left
 
            current = stack.pop()
            print(current.data, end=" ")
            current = current.right
 
    def preorder_non_recursive(self):
        if self.root is None:
            return
 
        stack = [self.root]
 
        while stack:
            current = stack.pop()
            print(current.data, end=" ")
 
            # Push right first so that left is processed first.
            if current.right is not None:
                stack.append(current.right)
            if current.left is not None:
                stack.append(current.left)
 
 
def main():
    bst = BinarySearchTree()
 
    n = int(input("Enter number of student records: "))
    for i in range(n):
        roll_no = int(input("Enter student roll number: "))
        bst.root = bst.insert(bst.root, roll_no)
 
    print("\\nStudent Records (Inorder - Ascending):")
    bst.inorder_non_recursive()
 
    print("\\nStudent Records (Preorder - Root First):")
    bst.preorder_non_recursive()
    print()
 
 
if __name__ == "__main__":
    main()
