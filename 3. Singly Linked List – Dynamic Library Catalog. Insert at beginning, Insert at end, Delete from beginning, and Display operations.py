from collections import deque
 
 
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
 
 
class BinarySearchTree:
    def __init__(self):
        self.root = None
 
    def insert(self, root, value):
        if root is None:
            return Node(value)
 
        if value < root.data:
            root.left = self.insert(root.left, value)
        elif value > root.data:
            root.right = self.insert(root.right, value)
        else:
            print("Duplicate Employee ID is not allowed.")
 
        return root
 
    def copy_tree(self, root):
        if root is None:
            return None
 
        new_node = Node(root.data)
        new_node.left = self.copy_tree(root.left)
        new_node.right = self.copy_tree(root.right)
        return new_node
 
    def level_order(self, root):
        if root is None:
            print("Tree is Empty")
            return
 
        queue = deque([root])
        while queue:
            current = queue.popleft()
            print(current.data, end=" ")
 
            if current.left is not None:
                queue.append(current.left)
            if current.right is not None:
                queue.append(current.right)
        print()
 
    def height(self, root):
        if root is None:
            return -1
 
        left_height = self.height(root.left)
        right_height = self.height(root.right)
        return max(left_height, right_height) + 1
 
    def print_leaf_nodes(self, root):
        if root is None:
            return
 
        if root.left is None and root.right is None:
            print(root.data, end=" ")
            return
 
        self.print_leaf_nodes(root.left)
        self.print_leaf_nodes(root.right)
 
 
def main():
    bst = BinarySearchTree()
    copied_root = None
 
    while True:
        print("\\n========== Employee Database using BST ==========")
        print("1. Insert Employee IDs")
        print("2. Display Original BST (Level Order)")
        print("3. Copy BST")
        print("4. Display Copied BST (Level Order)")
        print("5. Find Height of BST")
        print("6. Display Leaf Nodes")
        print("7. Exit")
 
        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Please enter a valid number.")
            continue
 
        if choice == 1:
            try:
                n = int(input("Enter number of employee IDs: "))
                if n < 0:
                    print("Number of IDs cannot be negative.")
                    continue
                for _ in range(n):
                    value = int(input("Enter Employee ID: "))
                    bst.root = bst.insert(bst.root, value)
            except ValueError:
                print("Please enter valid integer IDs.")
 
        elif choice == 2:
            print("Original BST (Level Order):")
            bst.level_order(bst.root)
 
        elif choice == 3:
            copied_root = bst.copy_tree(bst.root)
            print("BST Copied Successfully.")
 
        elif choice == 4:
            print("Copied BST (Level Order):")
            bst.level_order(copied_root)
 
        elif choice == 5:
            print("Height of BST =", bst.height(bst.root))
 
        elif choice == 6:
            print("Leaf Nodes are:")
            if bst.root is None:
                print("Tree is Empty")
            else:
                bst.print_leaf_nodes(bst.root)
                print()
 
        elif choice == 7:
            print("Exiting Program...")
            break
 
        else:
            print("Invalid Choice. Please try again.")
 
 
if __name__ == "__main__":
    main()
