class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def insert(root, value):
    if root is None:
        return TreeNode(value)
    else:
        if value < root.value:
            root.left = insert(root.left, value)
        else:
            root.right = insert(root.right, value)
    return root

def inorder_traversal(root):
    if root:
        inorder_traversal(root.left)
        print (root.value)
        inorder_traversal(root.right)

def preorder_traversal(root):
    if root:
        print (root.value)
        preorder_traversal(root.left)
        preorder_traversal(root.right)

def postorder_traversal(root):
    if root:
        postorder_traversal(root.left)
        postorder_traversal(root.right)
        print (root.value)

def printTree(node, level=0):
    if node != None:
        printTree(node.left, level + 1)
        print(' ' * 4 * level + '-> ' + str(node.value))
        printTree(node.right, level + 1)

# Example usage:
root = None
values = [5, 3, 7, 2, 4, 6, 8]

for value in values:
    root = insert(root, value)
print ("preorder_traversal\n")
preorder_traversal(root)
print ("\nInorder_traversal\n")
inorder_traversal(root)
print ("\nPostorder_traversal\n")
postorder_traversal(root)
printTree(root)